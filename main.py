
import sys
import os
from tag2_symbol import*
from colorama import Fore, Style

class PDAProcessor:
    def __init__(self):
        self.language = "" # language as one string, irrelevent after last update (to fufill bonus, I have decided to use an array of array of tokens rather than a string of tokens)
        self.state_found = 0 # save PDA's current state, 0 for non-accepted language, 1 for accepted language, irrelevant after last update (to fufill bonus, I will check whether or not a language is accpeted by using the failed_state property)
        self.start_state = "" # save start state
        self.stack_start_symbol = "" # save start stack symbol
        self.final_states = [] # save final states of PDA
        self.type_accept = "" # save PDA type of acceptence, F for final state, E for empty stack
        self.productions = {} # save PDA productions
        self.each_line = [] # store each line of html string (not edited, split with \n)
        self.language_per_line  = [] # matrix data structure, array of array of tokens, each element of matrix corresponds to the tokens of a particular line.
        self.failed_state = [] # save the state, input, and stack when PDA fails, 
        self.curr_line = 0 # save how many lines PDA have checked, stops increment when PDA fails
        self.current_state = [] # save current state of PDA
    
    def print_html_file(self):
        for line in self.each_line:
            print(line)
        print()

    def accpet_by_empty(self,state,language, stack):
        
        if len(language) != 0:
            return 0
        # elif (self.type_accept == "E"):
        #     return len(stack) < 1 # language sudah kosong dan stack sudah kosong
        else:
            self.current_state = [state,language,stack]
        # return state in self.final_states
    
    def get_moves(self, state, input_str, stack):
        moves = []

        for product in self.productions:
            if product != state:
                continue

            for j in self.productions[product]:
                current = j # current state
                new = [j[2]] # possible next state

                if current[0] : # if input is not epsilon
                    if input_str and input_str[0] == current[0]: # if input string is not empty and current input is the same as input in productions (transition function)
                        new.append(input_str[1:])
                    else:
                        continue
                else: # if input is epsilon
                    new.append(input_str)

                if current[1]: # check if top of stack is the same as in productions
                    if stack and stack[0] == current[1]:
                        new.append(current[3] + stack[1:])
                    else:
                        continue
                else:
                    new.append(current[3] + stack)

                moves.append(new)  # consist of current sate and remaining input, as well as the new top of the stack
                

        return moves

    def display_state(self, state, language, stack):
        print(f"Current State: {state}, Remaining Input: {language}, Stack: {stack}")

    def isAccepted(self, state, language, stack, config):
        # self.display_state(state, language, stack)  # Display current state
        
        if self.state_found:
            return False
        if self.accpet_by_empty(state, language, stack):
            self.state_found = 1
            return True

        possible_moves = self.get_moves(state, language, stack)
        if not possible_moves and len(language) != 0:
            print(f"Failed at State: {state} with Input: {language} and Stack: {stack}")
            print()
            self.failed_state = [state,language,stack]
            
            return False

        for move in possible_moves:
            if not self.isAccepted(move[0], move[1], move[2], config + [(move[0], move[1], move[2])]):
                # As soon as one path fails, return False to indicate the language is not accepted
                return False

        return False  # If all paths fail, return False

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
        if (self.failed_state != []): # if PDA fails, it will store its last state, input, and stack at the failed_state property
            print("Syntax Error")
            print(f"Failed at line {self.curr_line} : {self.each_line[self.curr_line-1].strip()}")
            print()
            if (len(self.failed_state[2]) >0):
                print("Possible transitions: ")
                # print out all possible fix :
                current_state = self.failed_state[0]
                current_top_stack = self.failed_state[2][0]
                possible_transitions = []
                possible_next_inputs = []
                possible_outcomes = self.productions[current_state]
                for transition in possible_outcomes:
                    if (current_top_stack == transition[1]):
                        possible_transitions.append(transition)
                        possible_next_inputs.append(transition[0])
                print(possible_transitions)
                print()

                print("Expected next inputs : ")
                print(possible_next_inputs)
                print()

            print("Possible error: ")
            # print()
            for line in self.each_line[0:self.curr_line-1]:
                print(line)
                
            print_with_color(self.each_line[self.curr_line-1],91)
            print()
            if (len(self.each_line[self.curr_line:]) > 5):
                for line in self.each_line[self.curr_line:self.curr_line+4]:
                    print(line)
                print("......")
            else:
                for line in self.each_line[self.curr_line:]:
                    print(line)
            print()

            
            
        elif (self.current_state == []):

            if (self.type_accept == "E"):
                print("Accepted")
                print()
                print("Your HTML file:")
                print()
                self.print_html_file()
            else :
                print("Syntax Error")
                print("Possible reason : Empty file")
        elif (self.current_state[1] == [] and len(self.current_state[2] ) < 1 and self.type_accept == "E"):
            print("Accepted")
            print()
            print("Your HTML file:")
            print()
            self.print_html_file()
        elif (self.current_state[1] == [] and (self.current_state[0] in self.final_states)):
            print("Accepted")
            print()
            print("Your HTML file:")
            print()
            self.print_html_file()
        else:
            print("Syntax Error")
        
    def string_to_one_line(self):
        lst=list(self.language)
        str=''
        for i in lst:
            str+=i
            lst1=str.split("\n")
            str1=""

        self.each_line = lst1
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
                print("PDA File needs to be txt")
                sys.exit(1)
        else:
            print("File doesn't exist")
            sys.exit(1)

        if os.path.exists(path_to_data + sys.argv[2]):
            if (sys.argv[2].endswith(('.html')) or sys.argv[2].endswith(('.txt'))):
                path_to_html = path_to_data + sys.argv[2]
            else:
                print(f"File {sys.argv[2]} is neither a html file or txt file")
                sys.exit(1)
        else:
            print("File doesn't exist")
            sys.exit(1)

        with open(path_to_html, 'r', encoding='utf-8') as html_file:
            html_content = html_file.read()
        html_content = normalize_html_file_content(html_content)

        self.language = html_content
        if (len(self.language) != 0):
            self.string_to_one_line() # jika ingin file dalam one line


        self.read_file_pda(path_to_text)
        self.language = tokenization(self.language)
        for line in self.each_line:
            self.language_per_line.append(tokenization(line))
        print()
        print("  EEEE Y   Y  FFFFF")
        print("  E     Y Y   F")
        print("  EEE    Y    FFFF")
        print("  E      Y    F")
        print("  EEEE   Y    F")
        print()
        print("HTML SYNTAX CHECKER")

        print()
        print()
        print("PDA tokens : ")
        print(self.language)
        print()
        print("Processing.......")

        for arr_tokens in self.language_per_line:
            if (self.failed_state == []):
                self.curr_line += 1
            if (arr_tokens != []): # possible space
                if (self.failed_state == []):
                    
                    if (self.curr_line == 1 or self.current_state == []):
                        self.isAccepted(self.start_state,arr_tokens,self.stack_start_symbol,[(self.stack_start_symbol,self.language,self.stack_start_symbol)])
           
                    else:
                        self.isAccepted(self.current_state[0],arr_tokens,self.current_state[2],[self.current_state[2],arr_tokens,self.current_state])
                else:
                    break
        self.check()


PDA_html = PDAProcessor()
PDA_html.run()