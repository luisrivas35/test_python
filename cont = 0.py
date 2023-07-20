cont = 0
with open('output_file.txt', 'w') as file_out:
    for data in pr:
        if data not in pim:
            file_out.write(pr +'\n')
            cont=cont+1
            print(pr.rstrip())


file_out.close()
print("Total de componentes diferentes en PR: ", cont)