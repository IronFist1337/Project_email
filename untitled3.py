import Algorithmia 

f = open("text.txt")
f_1=open("text_1.txt")
f_2=open("text_2.txt")
f_3=open("text_3.txt")
f_4=open("text_4.txt")
f_5=open("text_5.txt")
a= f.readline()
b= f_1.readline()
c= f_2.readline()
d= f_3.readline()
e= f_4.readline()
g= f_5.readline()

input = {
  "sentence": a
}

input_1 ={
"sentence": b
}

input_2 ={
"sentence": c
}

input_3 ={
"sentence": d
}
input_4 ={
"sentence": e
}
input_5 ={
"sentence": g
}

client = Algorithmia.client('simiP5QjBSDxOwNcnXzIUq79ApX1')
algo = client.algo('nlp/LanguageIdentification/1.0.0')
response=algo.pipe(input)
lang=response.result[0]

print (lang["language"])

response=algo.pipe(input_1)
lang=response.result[0]

print (lang["language"])

response=algo.pipe(input_2)
lang=response.result[0]

print (lang["language"])

response=algo.pipe(input_3)
lang=response.result[0]

print (lang["language"])

response=algo.pipe(input_4)
lang=response.result[0]

print (lang["language"])

response=algo.pipe(input_5)
lang=response.result[0]

print (lang["language"])