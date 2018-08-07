#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Written by: * StoNeR 1776
# https://github.com/stoner1776/QIWIAPI/
from QIWIAPI import *
from time import sleep

print('''
==============================================================================
  ___    _____        _____                                           Stable 
 / _ \  |_ _\ \      / /_ _|                                            
| | | |  | | \ \ /\ / / | |   
| |_| |_ | | _\ V  V /_ | | _ 
 \__\_(_)___(_)\_/\_/(_)___(_)  //API //     [This script will allow you  to
 
perform transactions and transfers using only API, as well as a purse number 
QIWI purse.] //Soft by StoNeR 1776
==============================================================================

RESPONSIBILITY:

1.0. This software is provided  EXCLUSIVELY  in the evaluation as well as to 
     simplify access to transactions and transactions by  using the  API  on 
     their Wallets;
1.1. The author  of this software does  not  bear  NO  responsibility if the 
     script  is  misused;
1.2. Script is in beta testing, but it is fairly stable. 

1.3. Please  press  [Enter]  to  continue  you  agree with the  above points

''')

print('''Q.I.W.I.A.P.I. Software stable! [v.3.0] // Written by StoNeR 1776
     

     [Please enter the purse token to check the balance]
      
      ''')

token = input('Token: ')                       # https://qiwi.com/api
phone = input('Phone: ')
api = QApi(token=token, phone=phone)
print('Balanse [RUB]')
print(api.balance)
print('''
     [Please  enter  the purse  number, as  well  as the 
     amount  of the  transfer  and  comments  to  it...]
     ''')
account = input('Number: ')
amount = input('Money [min 2$]: ')
comment = input('сomment: ')
api.pay(account=account, amount=amount, comment=comment)

print('Сonfirmed!') 
print(api.balance)                   
print('''
==============================================================================
   _____ __        _   __     ____     __________________
  / ___// /_____  / | / /__  / __ \   <  /__  /__  / ___/
  \__ \/ __/ __ \/  |/ / _ \/ /_/ /   / /  / /  / / __ \ 
 ___/ / /_/ /_/ / /|  /  __/ _, _/   / /  / /  / / /_/ / 
/____/\__/\____/_/ |_/\___/_/ |_|   /_/  /_/  /_/\____/  
                                                          www.stoner1776.pro        
==============================================================================
''')
