#This file is intended to simulate personalized rent prices provided by speciifc conditions
#As provided by the BLVD in Philomath, Oregon

#Total Rent in dollars
total_rent = 2250
utilities = 285
pet_fee = 35
master_fee = 0

def get_bool(prompt):
    while True:    
        status = input(prompt + '(Y/N): ').strip().lower()
        if status == 'y':
            return True
        elif status == 'n':
            return False
        else:
            print('Stop trying to thwart my program smh')
            continue

def main():
    pet = get_bool('Are you the primary caretaker of a pet? ')
    master = get_bool('Are you living in the master bedroom ')
    
    rent_with_pet = total_rent + (pet_fee if pet else 0)

    #Pull master surcharge out before splitting
    shared_rent = (rent_with_pet - master_fee) // 3
    personalized_rent = shared_rent + (master_fee if master else 0)

    #split utilities evenly
    personalized_utilities = utilities // 3

    print(f'\nYour rent is ${personalized_rent}')
    print(f'\nYour utilities cost is ${personalized_utilities}')
    print(f'\nYour total due is ${personalized_rent + personalized_utilities}\n')



if __name__ == '__main__':
    main()