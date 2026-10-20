# todo_cli.py  —— v0.1
# 功能：添加待办、查看待办
# 数据存在内存里，关掉程序就没了（v0.4 再解决持久化）

todos = []      # 所有待办都存在这个列表里，每条是一个字典


def add_todo(task):
    """添加一条待办"""
    todos.append({"task": task, "done": False})
    print(f"已添加：{task}")


def show_todos():
    """显示所有待办"""
    if not todos:
        print("还没有待办")
        return
    for i, todo in enumerate(todos, start=1):
        mark = "[x]" if todo["done"] else "[ ]"
        print(f"{i}. {mark} {todo['task']}")
def del_todos():
    show_todos()
    num=int(input("请输入要删除的待办事件的编号："))
    idx=num-1
    if 0 <= idx<len(todos):
        todos.pop(idx)
        print("删除成功")
    else:
        print("删除失败")





# 主程序：不断显示菜单，等用户选择
while True:
    print("\n===== 待办清单 =====")
    print("1. 添加待办")
    print("2. 查看待办")
    print("3. 删除代办")
    print("4. 退出")
    choice = input("请选择：")

    if choice == "1":
        task = input("要做什么：")
        add_todo(task)
    elif choice == "2":
        show_todos()
    elif choice == "3":
        del_todos()
        break
    elif choice == "4":
        print("再见")
    else:
        print("无效选择，请输入 1-4")