#MKHABELE MMM
#28/06/2023
def main():
   amount=int(50)
   while amount>0:
     print('Amount due: {}'.format(amount))
     insert=int(input('Insert amount: '))
     if insert==25 or insert==10 or insert==5:
        amount-=insert
     else:
        continue 
   print("Change Owed: {}".format(abs(amount)))
   
main()