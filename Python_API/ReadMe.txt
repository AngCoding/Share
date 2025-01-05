用Cursor打开此文件夹，安装Python插件后即可运行，
若不能运行，请安装python软件并更新python库
在cmd中输入指令：pip install matplotlib或pip install --user matplotlib

该python工程实现的功能：
提取Rte.c文件中以Rte_Get为前缀的函数名，提取返回类型和参数，存放至一个新的文本文件中，命名为Rte_Rx.c
提取以Rte_Set为前缀的函数名，存放至Rte_Tx.c中