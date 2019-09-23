#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql
import random

def words_infor(word, translation):
    '''
    函数功能：向单词信息表中插入数据
    函数描述：
    word：单词
    translation：注释
    返回值: 成功返回True, 失败返回False
    '''
    # 连接数据库
    conn = pymysql.connect("127.0.0.1", "azhe", "602661651nizhan$", "words")

    try:
        with conn.cursor() as cur:
            cur.execute("insert into words (word,translation) values (%s,%s)", (word, translation))
            r = cur.rowcount
            conn.commit()
    except:
        r = 0
    finally:
        conn.close()
    return bool(r)


def draft_infor(word, translation):
    '''
    函数功能：向草稿表中插入数据
    函数描述：
    word：单词
    translation：注释
    返回值: 成功返回True, 失败返回False
    '''
    # 连接数据库
    conn = pymysql.connect("127.0.0.1", "azhe", "602661651nizhan$", "words")

    try:
        with conn.cursor() as cur:
            cur.execute("insert into draft (word,translation) values (%s,%s)", (word, translation))
            r = cur.rowcount
            conn.commit()
    except:
        r = 0
    finally:
        conn.close()
    return bool(r)


def del_draft_infor():
    '''
    函数功能：删除草稿表中的信息
    函数描述：
    返回值: 成功返回True, 失败返回False
    '''
    # 连接数据库
    conn = pymysql.connect("127.0.0.1", "azhe", "602661651nizhan$", "words")

    try:
        with conn.cursor() as cur:
            cur.execute("delete from draft")
            r = cur.rowcount
            conn.commit()
    except:
        r = 0
    finally:
        conn.close()
    return bool(r)


def remember():
    '''
    函数功能：记词
    '''
    while True:
        print("-" * 30)
        
        input_word = input("请输入单词：")
        input_translation = input("请输入注释: ")

        # 判断两张表是否都插入成功
        if words_infor(input_word, input_translation) and draft_infor(input_word, input_translation):
            print("插入成功")
        else:
            print("插入失败")
        m = input("退出(q)")
        if m == "q":
            main()
            break
        print("-" * 30)


list1 = []
def write_memory():
    '''
    函数功能：默写
    '''
    # 连接数据库
    conn = pymysql.connect("127.0.0.1", "azhe", "602661651nizhan$", "words")
    cur = conn.cursor()
    cur.execute("select * from draft")
    rows = cur.fetchall()
    # print(rows)

    # 得到草稿里的所有单词
    try:
        n = 0
        while n < len(rows):
            word = rows[n][0]
            translation = rows[n][1]
            list1.append([word, translation])
            n += 1

        # 随机抽取单词或注释输出
        while True:
            x = random.randint(0, len(list1) - 1)
            y = random.randint(0, 1)
            print("-" * 30)
            print("默写另一半")
            print(list1[x][y])
            input_write_memory = input(">")
            #判断是否默写正确
            if y == 0:
                y = 1
            else:
                y = 0
            if input_write_memory == list1[x][y]:
                print("默写正确")
                m = input("退出(q)")
                if m == "q":
                    main()
                    break
            else:
                print("默写错误！！！")
                print("正确的答案是: " + list1[x][y])
                input("你要再记下这个单词，按回车继续")
                m = input("退出(q)")
                if m == "q":
                    main()
                    break
            print("-" * 30)
    except:
        print("您今天还没有记词，无默写内容！")
        main()
    

list2 = []
def review_write_memory():
    '''
    函数功能：回顾默写
    '''
    # 连接数据库
    conn = pymysql.connect("127.0.0.1", "azhe", "602661651nizhan$", "words")
    cur = conn.cursor()
    cur.execute("select * from words")
    rows = cur.fetchall()
    # print(rows)

    # 得到单词表里的所有单词
    n = 0
    while n < len(rows):
        word = rows[n][0]
        translation = rows[n][1]
        list2.append([word, translation])
        n += 1

    # 随机抽取单词或注释输出
    while True:
        x = random.randint(0, len(list2) - 1)
        y = random.randint(0, 1)
        print("-" * 30)
        print("默写另一半")
        print(list2[x][y])
        input_write_memory = input(">")
        #判断是否默写正确
        if y == 0:
            y = 1
        else:
            y = 0
        if input_write_memory == list2[x][y]:
            print("默写正确")
            m = input("退出(q)")
            if m == "q":
                main()
        else:
            print("默写错误！！！")
            print("正确的答案是：" + list2[x][y])
            input("你要再记下这个单词，按回车继续")
            if m == "q":
                main()
                break
        print("-" * 30)


def main():
    print('''欢迎使用azhe记词程序！！！
    请输入操作序号：
        1.记词  2.默写  3.回顾默写  4.退出
    ''')

    n = int(input("> "))
    if n == 1:
        remember()
    if n == 2:
        write_memory()
    if n == 3:
        review_write_memory()
    if n == 4:
        del_draft_infor()
        print("欢迎下次再来！")



if __name__ == '__main__':
    main()

