import time

def Suborder():
    print("The order processing is followed by choosing the bread/wraps/salad bowl options, sizes, protein, veggies, dressings, and salt & pepper")
    
    options = input("what would you like your sub in: bread, wrap or salad bowl").lower()
    protein_prices = {
        "footlong": {
            'chicken teriyaki': 14.45,
            'buffalo chicken': 14.45,
            'smoked pork belly': 15.50,
            'pulled pork': 15.25,
            'turkey': 12.00,
            'pizza sub': 9.95,
            'seafood': 12.95,
        },
        "Six inch": {
            'chicken teriyaki': 9.45,
            'buffalo chicken': 9.45,
            'smoked pork belly': 9.80,
            'pulled pork': 9.55,
            'turkey': 6.00,
            'pizza sub': 5.95,
            'seafood': 7.95,
        }
    }
    veggies_prices = {
        'footlong': {
            'lettuce' : 0.00,
            'spinach' : 0.00,
            'carrot' : 0.00,
            'cucumber':0.00,
            'pineapple_is_extra': 1.00,
            'beetroot_is_extra': 1.00,
            'avocado_is_extra': 2.50,
        },
        'Six inch': {
            'lettuce' : 0.00,
            'spinach' : 0.00,
            'carrot' : 0.00,
            'cucumber':0.00,
            'pineapple_is_exxtra': 0.50,
            'beetroot_is_exxtra': 0.50,
            'avocado_is_exxtra': 1.25,
        },
    }
    sn_prices={
        'meatball mozza pot':4.25,
        "cheesy garlic toastie": 3.95,
        "avocado toastie": 3.50,
        "southern style chicken bites":4.50,
        "ham and tomato toaste":3.50,
    }
    
    
    def protein_selection():
        selected_protein = []
        size = input("What size  (footlong or Six inch)? ").lower()
        if size in protein_prices:
            print("Available proteins for", size, "sandwich:")
            for protein in protein_prices[size]:
                print(protein)
            request = input("What protein would you like? ").lower()
            print(request)
            selected_protein = [protein.strip() for protein in request.split(",")]
            print("Selected protein:", ", ".join(selected_protein))
            if request in protein_prices[size]:
                print("Sure")
                return protein_prices[size][request]
            else:
                print("Wait a moment, let me confirm")
                time.sleep(2)
                print(request, "Sorry this protein is not available ")
                quit()
        else:
            print("Size not available.")
            quit()


    def veggies_selection():
        selected_veggies = []
        size = input('Could you please confirm the size again: footlong or six inch?').lower()
        veggies_choices = veggies_prices[size]
        print("Choose your veggies from the following list (separate with commas):")
        for veggie in veggies_choices:
            print(veggie)
        request = input("What veggies are you after?").lower()
        selected_veggies = [veggie.strip() for veggie in request.split(",")]

        total_veggie_price = sum(veggies_choices.get(veg, 0) for veg in selected_veggies)
        print("Selected Veggies:", ", ".join(selected_veggies))
        return total_veggie_price


    def dressing_selection():
        dressing_choices = ['marinara', 'bbq', 'Aioli', 'sweet onion', 'sweet chilli', 'hot habanero', 'Blue cheese']
        selected_dressing = []
        print(dressing_choices)
        request = input("What dressings are you after? (separate with commas): ").lower()
        selected_dressing = [dressing.strip() for dressing in request.split(",")]
        print("Selected Dressings:", ", ".join(selected_dressing))
        time.sleep(3)
        print("Thanks for ordering from subway.. You may proceed to the register")
    
    def loyal_customer():
        request = input(print("Do you have a membership card on you?"))
        if request == 'yes'.lower():
            print("you may scan your card to redeem the points")
        else:
            print("Do you want one?")
        
        
    def snack_selection():
        print("we also have snack options as well")
        sn_choices=["meatball mozza pot", "cheesy garlic toastie", "ham cheese and tomato toaste", "avocado toastie", "southern style chicken bites"]  
        print(sn_choices)
        for snack in sn_prices:
            print(snack)
        request = input("what snacks would you like?") 
        if request in sn_prices:
            print("sure")
        selected_snacks = [snack.strip() for snack in request.split(",")]

        total_snack_price = sum(sn_prices.get(sn, 0) for sn in selected_snacks)
        print("Selected snacks:", ", ".join(selected_snacks))
        print("Total snacks Price: $", total_snack_price)
        return total_snack_price 
      
               
                
    if options == 'bread':
        def bread_selection():
            print("The bread choices we have are:")
            bread_choices = ["italian herbs and cheese", "malted Rye and seasoned grain", "wheat", "white"]
            print(bread_choices)
            request = input("So, What bread would you like? ")
            print(request)
            if request in bread_choices:
                print("Sure")
                protein_price = protein_selection()
                veggies_price = veggies_selection()
                dressing_selection()
                sn_prices = snack_selection()
                
                total_price =  protein_price + veggies_price + sn_prices
                print(f"The total price is : ${total_price:.2f}")

                loyal_customer()

                print(f"you have {total_price} points")

            else:
                print("Wait a moment, let me confirm")
                time.sleep(2)
                print(request, "Sorry this bread is not available ")
                quit()

        bread_selection()
    
    if options == 'wrap':
        def wrap_selection():
            wrap_choices = ["Multigrain", "plain white"]
            print(wrap_choices)
            request = input("So, What wrap would you like? ")
            print(request)
            if request in wrap_choices:
                print("Sure")
                protein_price = protein_selection()
                veggies_price = veggies_selection()
                dressing_selection()
                sn_prices = snack_selection()
                
                total_price =  protein_price + veggies_price + sn_prices
                print(f"The total price is : ${total_price:.2f}")

                loyal_customer()
                print(f"you have {total_price} points")

                
                

                
                   

            else:
                print("Wait a moment, let me confirm")
                time.sleep(2)
                print(request, "Sorry this wrap is not available ")
                quit()
        wrap_selection()
    
    if options == 'salad bowl':
        def salad_bowl_selection():
            print(" We have two sizes of salad bowl: Regular and large")
            print("Regular sald bowl contains the six inch portion and large salad bowl contains the footlong portion")
            sb_choices=['Regular', 'large']
            print(sb_choices)
            request = input("so, which salad bowl would you like?")
            if request in sb_choices:
                print("sure")
                protein_price = protein_selection()
                veggies_price = veggies_selection()
                dressing_selection()
                sn_prices = snack_selection()
                
                total_price =  protein_price + veggies_price + sn_prices
                print(f"The total price is : ${total_price:.2f}")
                loyal_customer()
                print(f"you have {total_price} points")


            else:
                print("Wait a moment, let me confirm")
                time.sleep(2)
                print(request, "Sorry this salad bowl is not available ")
                quit()
        salad_bowl_selection()       

         
        
    
    
    

Suborder()