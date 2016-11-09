
                    ########readiang a file#########
helloFile=open(r'F:/hello.txt')
helloContent=helloFile.read()
print(helloContent)

writeFile1=open(r'F:/write.txt')
writeFile1Content=writeFile1.read()
writeFile1.close()


writeFile2=open(r'F:/write.txt','w')
writeFile2.write(helloContent)
writeFile2.close()

writeFile3=open(r'F:/write.txt','a')
writeFile3.write(writeFile1Content)
writeFile3.close()

writeFileContent=open(r'F:/write.txt')
print(writeFileContent.read())

#### The above program is gona write the content at the beginging of the file