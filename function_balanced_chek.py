from class_Stack import Stack


stack = Stack()
#функция проверки сбалансированности скобок
def balanced_check(brackets):
   for br in brackets:
      if br in '({[':
         stack.push(br)
      if br in ')}]':
         if stack.size() == 0:
             return 'Unbalanced'
         elif br == ')' and stack.pop() == '(':
             continue
         elif br == '}' and stack.pop() == '{':
             continue
         elif br == ']' and stack.pop() == '[':
             continue
         else:
             return 'Unbalanced'
   if stack.is_empty() == False:
       return 'Unbalanced'
   else:
       return 'Balanced'






