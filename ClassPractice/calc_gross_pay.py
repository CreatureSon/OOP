TAX_RATE = 0.15
TIME_AND_HALF = 1.5

def main():
    h,r = get_input()
    gross_pay = calc_gross_pay(h,r)
    ot_pay = calc_overtime_pay(r)
    t,b = calc_withholdings(gross_pay,ot_pay)
    net_pay = calc_net_pay(gross_pay,ot_pay,t,b)
    print_paycheck(net_pay)

def get_input():
    hrs = get_hrs_worked()
    payrate = get_pay_rate()

    return hrs,payrate


def get_hrs_worked():
    hrs = float(input("Please enter number of hours worked: "))

    return hrs


def get_pay_rate():
    payrate = float(input("Please enter your payrate: "))

    return payrate


def calc_gross_pay(hrs,payrate):
    gross_pay = payrate * hrs

    return gross_pay


def calc_overtime_pay(payrate):
    ot_hrs = float(input("Please enter number of hours worked overtime: "))
    ot_pay = payrate * TIME_AND_HALF * ot_hrs

    return ot_pay

def calc_withholdings(gross_pay,ot_pay):
    tot_taxes = calc_taxes(gross_pay,ot_pay)
    benefits = calc_benefits()

    return tot_taxes, benefits

def calc_taxes(gross_pay,ot_pay):
    total_pay = gross_pay + ot_pay
    tot_taxes = total_pay * TAX_RATE

    return tot_taxes

def calc_benefits():
    benefits_amt = float(input("Enter total amt. of benefits: "))

    return benefits_amt
                         


def calc_net_pay(gross_pay,ot_pay,tot_taxes, benefits):

    net_pay = gross_pay + ot_pay - tot_taxes - benefits

    return net_pay


def print_paycheck(net_pay):

    print("The amount of your paycheck is: $",format(net_pay,",.2f"),sep='')
    

main()
    












    
