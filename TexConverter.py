import os
import sys

def error(line_num, line, error_msg):
    assert("line : " + str(line_num) +"\n"
                            + line + "\n" +
                            "ERROR : " + error_msg)

def search(dirname) :
    targets = []
    try :    
        filenames = os.listdir(dirname)
        for filename in filenames :
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename) :
                targets.extend(search(full_filename))
            ext = os.path.splitext(full_filename)[-1]
            rest = os.path.splitext(full_filename)[-2]
            front_ext = os.path.splitext(rest)[-1]
            if front_ext == '.tex' and ext == '.md':
                targets.append(full_filename)
                print("target : " + str(full_filename))
    except PermissionError:
        pass
    return targets


def makeURLCode(equation) :
    
    def to_escapecode(equation, character) :
        def escapeCode(character) :
            return "%" + format(ord(character), "x")
        return equation.replace(character, escapeCode(character))
    
    equation = to_escapecode(equation, ' ')
    #equation = to_escapecode(equation, '!')
    #equation = to_escapecode(equation, '"')
    #equation = to_escapecode(equation, '#')
    #equation = to_escapecode(equation, '%')
    #equation = to_escapecode(equation, '&')
    #equation = to_escapecode(equation, '\'')
    #equation = to_escapecode(equation, '(')
    #equation = to_escapecode(equation, ')')
    #equation = to_escapecode(equation, '*')
    #equation = to_escapecode(equation, '+')
    #equation = to_escapecode(equation, ',')
    #equation = to_escapecode(equation, '-')
    #equation = to_escapecode(equation, '.')
    #equation = to_escapecode(equation, '/')
    #equation = to_escapecode(equation, ':')
    #equation = to_escapecode(equation, ';')
    #equation = to_escapecode(equation, '<')
    #equation = to_escapecode(equation, '=')
    #equation = to_escapecode(equation, '>')
    #equation = to_escapecode(equation, '?')
    #equation = to_escapecode(equation, '@')
    #equation = to_escapecode(equation, '[')
    #equation = to_escapecode(equation, ']')
    #equation = to_escapecode(equation, '\\')
    #equation = to_escapecode(equation, '{')
    #equation = to_escapecode(equation, '}')
    #equation = to_escapecode(equation, '|')
    #equation = to_escapecode(equation, '^')
    #equation = to_escapecode(equation, '_')
    #equation = to_escapecode(equation, '`')
    #equation = to_escapecode(equation, '~')
    return equation


def convert(filename) :
    file = open(filename, 'rt', encoding='UTF8')
    new_filename = os.path.splitext(filename)[-2]
    new_filename = os.path.splitext(new_filename)[-2]
    new_filename = new_filename + '.md'
    newfile = open(new_filename, 'w', encoding='UTF8')
    line_num = 0

    math_token = 0
    math_start = 0

    new_line = ""
    math_line = ""
    
    while True:
        line = file.readline()
        if not line: break
        line_num += 1

        for ch in line :
            if ch == '$':
                math_token += 1
            else :
                if math_token == 0 :
                    if math_start >= 1 :
                        math_line += ch
                    else :
                        new_line += ch
                elif math_token == 1:
                    if math_start == 0 :
                        math_line += ch
                        math_start = 1
                        math_token = 0
                    elif math_start == 1 :
                        math_start = 0
                        math_token = 0
                        
                        math_line = makeURLCode(math_line)
                        #new_line += "![](https://latex.codecogs.com/gif.latex?" + math_line + ")"
                        new_line += "<img src=\"https://latex.codecogs.com/gif.latex?" + math_line + "\">" 
                        math_line = ""
                        new_line += ch

                    else : #math_start == 2 
                        error(line_num, line, "start $$, but end $")
                elif math_token == 2:
                    if math_start == 0:
                        math_line += ch
                        math_start = 2
                        math_token = 0
                    elif math_start == 1:
                        error(line_num, line, "start $, but end $$")
                    else : #math_start == 2
                        new_line += ch
                        math_start = 0
                        math_token = 0
                        
                        math_line = makeURLCode(math_line)
                        #new_line += "![](https://latex.codecogs.com/svg.latex?" + math_line + ")"
                        new_line += "<p align=\"center\"><img src=\"https://latex.codecogs.com/gif.latex?" + math_line + "\"></p>"
                        math_line = ""
                        new_line += ch

                else :
                    error(line_num, line, "TOKEN($) Overuse")
                      
        print(new_line, end='')
        newfile.write(new_line)
        new_line = ""
    
    file.close()
    newfile.close()

def massive_convert(filenames) :
    for filename in filenames :
        convert(filename)
        
if __name__ == "__main__" :
    if len(sys.argv) == 1 :
        targets = search(".")
    else :
        targets = search(sys.argv[1])
    massive_convert(targets)
    