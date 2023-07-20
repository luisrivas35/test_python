#!/usr/bin/env python3
#author:Luis Rivas
#script to compare two .txt files and find the no match components
cont = 0
with open('pimfile.txt', 'r') as a:
    pim = set(a)
    with open('prfile.txt', 'r') as b:
        
        with open('output_file.txt', 'w') as file_out:
            for pr in b:
                if pr not in pim:
                    file_out.write(pr +'\n')
                    cont=cont+1
                    print(pr.rstrip())


file_out.close()
print("Total de componentes diferentes en PR: ", cont)