# Written by evan holloway
# Date Written March 20 2023
# One Stop insurance company project for QAP4


import datetime

# Open OSICDef.dat and read the data
with open('OSICDef.dat', 'r') as f:
    NEXT_POLICY_NUM_RATE = int(f.readline())
    BASIC_PREMIUM = float(f.readline())
    DISCOUNT_PER_ADD_CAR = float(f.readline())
    EXTRA_LIABILITY_COVERAGE = float(f.readline())
    GLASS_COVERAGE = float(f.readline())
    LOANER_CAR_COVERAGE = float(f.readline())
    HST_RATE = float(f.readline())
    PROCESSING_FEE_MONTH = float(f.readline())

# Valid provinces list
Provinces = ['AB', 'BC', 'MB', 'NB', 'NL', 'NT', 'NS', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT']
#start loop
while True:
# Prompt user for input
    FirstName = input("Enter customer's first name: ").title()
    LastName = input("Enter customer's last name: ").title()
    StreetAddress = input("Enter customer's address: ")
    City = input("Enter customer's city: ").title()
    Province = input("Enter customer's province (2 letter code): ").upper()

    while Province not in Provinces:
        Province = input("Invalid province code. Please enter a valid 2 letter code: ").upper()

    PostalCode = input("Enter customer's postal code (XXXXXX): ").upper()
    if len(PostalCode) != 6:
        PostalCode = input("Invalid Postal. Please enter a value equal to 6 characters: ")

    PhoneNum = input("Enter customer's phone number (9999999999): ")
    while not PhoneNum.isdigit() or len(PhoneNum) != 10:
        PhoneNum = input("Invalid phone number. Please enter a 10 digit number: ")

    NumCars = int(input("Enter the number of cars being insured: "))

    ExtraLiability = input("Do you want extra liability coverage up to $1,000,000? (Y/N): ").upper()
    if ExtraLiability == "":
        print(" this cannot be blank - please re-enter.")

    GlassCoverage = input("Do you want optional glass coverage? (Y/N): ").upper()
    if GlassCoverage == "":
        print(" This cannot be blank - please re-enter.")

    LoanerCar = input("Do you want optional loaner car coverage? (Y/N): ").upper()
    if LoanerCar == "":
        print(" this cannot be blank - please re-enter.")

    PaymentType = input("Do you want to pay in full or monthly? (F/M): ").upper()
    while PaymentType not in ['F', 'M']:
        PaymentType = input("Invalid payment type. Please enter 'F' for full payment or 'M' for monthly payments: ").upper()

# Calculate extra costs
    ExtraCosts = 0
    if ExtraLiability.upper() == "Y":
        ExtraCosts += 130.00 * NumCars
    elif GlassCoverage.upper() == "Y":
        ExtraCosts += 86.00 * NumCars
    elif LoanerCar.upper() == "Y":
        ExtraCosts += 58.00 * NumCars

# Calculate total insurance premium
    TotalPremium = BASIC_PREMIUM + (NumCars - 1) * BASIC_PREMIUM * DISCOUNT_PER_ADD_CAR + ExtraCosts

# Calculate HST and total cost
    Hst = HST_RATE * TotalPremium
    TotalCost = TotalPremium + Hst

# Calculate monthly payment
    ProcessingFee = PROCESSING_FEE_MONTH
    MonthlyPayment = (TotalCost + ProcessingFee) / 8


# Dates
    InvoiceDate = datetime.date.today()
    PaymentDate = datetime.date.today().replace(day=1) + datetime.timedelta(days=32)

# formatting a couple costs
    ExtraCostsDsp = "${:,.2f}".format(ExtraCosts)
    MonthlyPaymentDsp = "${:,.2f}".format(MonthlyPayment)

    print()
    print(f'             One Stop insurance company             ')
    print('-----------------------------------------------------')
    print(f'Customer Name: {FirstName:<10} {LastName:>10}')
    print(f'Phone Number:  {PhoneNum:>10}')
    print()
    print(f'Customer Address: {StreetAddress:<29s} ')
    print(f'                  {City:<19s} {Province:<2s} {PostalCode:<6s}')
    print('-----------------------------------------------------')
    print(f"Number of Cars: {NumCars:>1}   Extra Liability: {ExtraLiability:>1}")
    print(f"Glass Coverage: {GlassCoverage:>1}   Loaner Car Option:, {LoanerCar:>1}")
    print()
    print("Total Insurance Premium: $%.2f" % TotalPremium)
    print("HST: $%.2f" % Hst)
    print("Total Cost: $%.2f" % TotalCost)
    if PaymentType.upper() == "M":
        print(f"Monthly Payment: {MonthlyPaymentDsp:<9}  Extra Cost: {ExtraCostsDsp:>9}")
    print('-----------------------------------------------------')
    print(f'Invoice Date: {InvoiceDate}   Payment Date: {PaymentDate}')

    with open("Policies.dat", "a") as f:
        f.write("{}, ".format(str(NEXT_POLICY_NUM_RATE)))
        f.write("{}, ".format(InvoiceDate))
        f.write("{}, ".format(FirstName))
        f.write("{}, ".format(LastName))
        f.write("{}, ".format(StreetAddress))
        f.write("{}, ".format(City))
        f.write("{}, ".format(Province))
        f.write("{}, ".format(PostalCode))
        f.write("{}, ".format(NumCars))
        f.write("{}, ".format(ExtraLiability))
        f.write("{}, ".format(GlassCoverage))
        f.write("{}, ".format(LoanerCar))
        f.write("{}, ".format(PaymentType))
        f.write("{}\n".format(str(TotalPremium)))

        NEXT_POLICY_NUM_RATE += 1

        f.close()
        print()
        print('Policy information processed and saved.')


