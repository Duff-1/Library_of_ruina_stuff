import random

def test(p):
    page = open(f'{p}.txt','r')
    
    minimum = 0
    maximum = 0
    count = 0

    dicenum = 1
    
    dicevalues = {}
    
    for line in page:
        if line.strip('\n') == 'eod':
            
            dicevalues[f'dice{dicenum}'] = (minimum, maximum, dicetype)
            
            
            minimum = 0
            maximum = 0
            dicetype = ''
            dicenum = dicenum + 1
            
        else:
            try:
                match count:
                    case 0:
                        minimum = int(line.strip('\n'))
                        count = 1
                    case 1:
                        maximum = int(line.strip('\n'))
                        count = 0

            except:
                dicetype = line.strip('\n')
            
    print(dicevalues)
    print()
    return dicevalues

class dice:
    def __init__(self,min,max,bonus,dicetype):
        
        self.min = min
        self.max = max
        self.bonus = bonus        
        self.dicetype = dicetype
        self.base, self.mod, self.dicetype = self.roll()
        
    def roll(self):
        base = random.randint(self.min, self.max)
        mod = self.bonus + base
        
        return base, mod, self.dicetype

class card:
    def __init__(self,page):
        self.pagedice = test(page)
        self.dicelist= []
        
        self.rollpage()
        
    def rollpage(self):
        for i,b in enumerate(self.pagedice):
            minimum, maximum, dicetype = self.pagedice[b]
            self.dicelist.append(dice(minimum, maximum, checkbonus(dicetype), dicetype))
            
        count = 0
        for d in self.dicelist:
            tem = d.roll()
            base, maodif, dicetype = tem
            count+=1
            print(f'base: {base}\nmodified: {maodif}\ndicetype: {dicetype}')
            print()

class modifiers:
        slash = 1
        blunt = 1
        pierce = 1
        evade = 1
        block = 1

def checkbonus(dtype):
    match dtype:
        case 'slash':
            return modifiers.slash
        case 'blunt':
            return modifiers.blunt
        case 'pierce':
            return modifiers.pierce
        case 'evade':
            return modifiers.evade
        case 'block':
            return modifiers.block

def main():
    while True:
        temp = input('page name: ')
        ch = input('change modifiers? (y/n)')
        if ch == 'y':
            modifiers.slash = int(input('slash'))
            modifiers.pierce = int(input('pierce'))
            modifiers.blunt = int(input('blunt'))
            modifiers.evade = int(input('evade'))
            modifiers.block = int(input('block'))
        else:
            print(f'slash {modifiers.slash}, blunt {modifiers.blunt}, pierce {modifiers.pierce}, evade {modifiers.evade}, block {modifiers.block}\n')

        current_card = card(temp)
        current_card.rollpage

if __name__ == '__main__':
    main()