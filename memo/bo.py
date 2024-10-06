def format_text(text):
    indent_level = 0
    in_string = False
    result = []
    indent_str = "    "  # 4칸 들여쓰기

    for i, char in enumerate(text):
        if char == '"' or char == "'":
            if not in_string:
                in_string = char  # 문자열의 시작
            elif in_string == char:
                in_string = False  # 문자열의 끝
            result.append(char)
            continue
        
        if in_string:
            result.append(char)
            continue

        if char in "({[":
            result.append(char)
            indent_level += 1
            result.append("\n" + indent_str * indent_level)
        elif char in ")}]":
            indent_level -= 1
            result.append(char + "\n" + indent_str * indent_level)
        elif char in " \t\n":
            continue
        else:
            result.append(char)

    return ''.join(result)

def read_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return f"Error: The file '{file_name}' does not exist."
    except Exception as e:
        return f"An error occurred: {e}"
    
# 테스트 실행
# text = 'function(arg1, arg2) { if (condition) { return [1, 2, 3]; } }'
# formatted_text = format_text(text)
# print(formatted_text)

# import bo
# print (bo.format_text(bo.read_file("./tree-sitter-smallbasic/saved_lexical_grammar.txt")))

