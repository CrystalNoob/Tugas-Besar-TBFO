
import sys
import os
from bs4 import BeautifulSoup
from tag2_symbol import*
import html2text


class PDAProcessor:
    def __init__(self):
        self.language = ""
        self.state_found = 0 
        self.start_state = ""
        self.stack_start_symbol = ""
        self.final_states = []
        self.type_accept = ""
        self.productions = {}

    def accpet_by_empty(self,state,language, stack):
        if len(language) != 0:
            return 0
        elif (self.type_accept == "E"):
            return len(stack) < 1 # language sudah kosong dan stack sudah kosong
        return state in self.final_states
    
    def get_moves(self, state, input_str, stack):
        moves = []

        for product in self.productions:
            if product != state:
                continue

            for j in self.productions[product]:
                current = j
                new = [j[2]]

                if current[0] :
                    if input_str and input_str[0] == current[0]:
                        new.append(input_str[1:])
                    else:
                        continue
                else:
                    new.append(input_str)

                if current[1]:
                    if stack and stack[0] == current[1]:
                        new.append(current[3] + stack[1:])
                    else:
                        continue
                else:
                    new.append(current[3] + stack)

                moves.append(new)

        return moves

    def isAccepted(self,state,language,stack,config):
        total_in_stack = 0

        if self.state_found:
            return 0
        if self.accpet_by_empty(state,language,stack):
            self.state_found = 1
            return 1
        total_curr_move = self.get_moves(state, language, stack)
        if (total_curr_move == 0 ):
            return 0
        for move in total_curr_move:
            total_in_stack += self.isAccepted(move[0], move[1], move[2], config + [(move[0], move[1], move[2])])
        return total_in_stack

    def read_file_pda(self,file_path):
        try:
            with open(file_path, 'r') as file:
                lines = [line.rstrip() for line in file]
        except FileNotFoundError:
            return 0
        self.start_state = lines[3]
        self.stack_start_symbol = lines[4]
        self.final_states = lines[5].split()
        self.type_accept = lines[6].split()
        for i in range(7, len(lines)): # load productions
            production = lines[i].split()
            configuration1 = [(production[1], production[2],  production[3],production[4])]
            key = production[0]

            if key not in self.productions:
                self.productions[key] = []

            configuration2 = [tuple(production_input if production_input != "e" else "" for production_input in tup) for tup in configuration1]
            self.productions[key].extend(configuration2)


    def check(self):
        if self.state_found:
            print("Diterima")
        else:
            print("Tidak diterima")


    def string_to_one_line(self):
        lst=list(self.language)
        str=''
        for i in lst:
            str+=i
            lst1=str.split("\n")
            str1=""

        for i in lst1:
            str1+=i+" "
            str2=str1[:-1]
        self.language = str2

    def run(self): # read file path in command line
        if len(sys.argv) != 3:
            print("Something went wrong")
            sys.exit(1)
        path_to_data = "./data/"
        path_to_html = ""
        path_to_text = ""

        # Get the file paths from command-line arguments
        if os.path.exists(path_to_data + sys.argv[1]):
            if (sys.argv[1].endswith(('.txt'))):
                path_to_text = path_to_data + sys.argv[1]
            else:
                print("File is not txt")
                sys.exit(1)
        else:
            print("File doesn't exist")
            sys.exit(1)

        if os.path.exists(path_to_data + sys.argv[2]):
            if (sys.argv[2].endswith(('.html'))):
                path_to_html = path_to_data + sys.argv[2]
            else:
                print("File is not html")
                sys.exit(1)
        else:
            print("File doesn't exist")
            sys.exit(1)

        with open(path_to_html, 'r', encoding='utf-8') as html_file:
            html_content = html_file.read()

        self.language = html_content
        if (len(self.language) != 0):
            self.string_to_one_line() # jika ingin file dalam one line
        # with open("./data/html_in_text.txt","w") as f:
        #     f.write(self.language)


        self.read_file_pda(path_to_text)
        # print(self.language)
        # print(self.language)
        self.language = tokenization(self.language)
        print(self.language)
        # self.language = ['head','head','head','head','head','head']
        # self.language = ['TEXT','TEXT']
        # print(self.language)
        # self.transform_html_to_txt()
        print(self.productions)
        self.isAccepted(self.start_state,self.language,self.stack_start_symbol,[(self.stack_start_symbol,self.language,self.stack_start_symbol)])
        self.check()

k = PDAProcessor()
k.run()