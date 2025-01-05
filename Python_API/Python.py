import re

def extract_rte_functions(input_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 正则表达式匹配以Rte_Get或Rte_Set开头的函数定义
        pattern = r'(\w+\s+\*?\s*)?(Rte_(Get|Set)\w+)\s*\(([\w\s,*]*)\)'
        matches = re.finditer(pattern, content)
        
        # 分别存储Get和Set函数信息
        get_functions = []
        set_functions = []
        
        for match in matches:
            return_type = match.group(1).strip() if match.group(1) else 'void'
            function_name = match.group(2)
            parameters = match.group(4).strip()
            
            # 格式化函数定义
            function_def = f"{return_type} {function_name}({parameters});"
            
            # 根据函数前缀分类存储
            if function_name.startswith('Rte_Get'):
                get_functions.append(function_def)
            elif function_name.startswith('Rte_Set'):
                set_functions.append(function_def)
        
        # 写入Get函数到Rte_Rx.c
        with open('Rte_Rx.c', 'w', encoding='utf-8') as f:
            f.write("/* Generated Rte Get Functions */\n\n")
            for func in get_functions:
                f.write(func + '\n')
        
        # 写入Set函数到Rte_Tx.c
        with open('Rte_Tx.c', 'w', encoding='utf-8') as f:
            f.write("/* Generated Rte Set Functions */\n\n")
            for func in set_functions:
                f.write(func + '\n')
        
        print(f"Successfully extracted {len(get_functions)} Rte_Get functions to Rte_Rx.c")
        print(f"Successfully extracted {len(set_functions)} Rte_Set functions to Rte_Tx.c")
        
    except FileNotFoundError:
        print(f"Error: Could not find the input file {input_file}")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

# 使用函数
extract_rte_functions('Rte.c')
