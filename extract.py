
def pull( filename ):

    with open(filename) as file:
        lines = file.readlines()

    return lines

def extract():

    sAndP = pull( 'big' )
    # techCompanies = pull( 'companylist' )
    # techCompanies = techCompanies[1:len(techCompanies)]
    techCompanies = ['ADBE','AMD','GOOG','ADI','AAPL','AMAT','ADSK','ADP','CA','CERN','CSCO','CTXS','CTSH',
                     'CSC','CVG','DOV','ETN','FSLR','FISV','HPQ','ITW','INTC','IBM','IPG','INTU','JBL','JNPR',
                     'LLL','LLTC','MCHP','MU','MSFT','NTAP','NVDA','OMC','ORCL','QCOM','RHT','RHI','CRM','SYMC',
                     'TDC','TXN','VRSN','WDC','XLNX','YHOO']

    destination = open( 'extracted', 'w')

    acc = 0

    for company in techCompanies:

        # parts = company.split(',')
        # symbol =  parts[0].strip("\"")
        # name = parts[1]


        # results = binarySearch(symbol, sAndP, 0, len(sAndP))
        results = binarySearch(company, sAndP, 0, len(sAndP))

        if results != None:
            acc+=1
            for price in results:
                destination.write( price )
    print(acc)


def binarySearch( symbol, lines, start, end ):

    midpoint = int((end-start)/2) + start
    compared = lines[midpoint].split(',')[0]

    if midpoint == start or midpoint == end:
        return None

    elif symbol == compared:

        topIndex = midpoint
        bottomIndex = midpoint

        #Find above
        while lines[topIndex-1].split(',')[0] == symbol:
            topIndex-=1

        #Find below
        while lines[bottomIndex+1].split(',')[0] == symbol:
            bottomIndex+=1

        return lines[topIndex:bottomIndex+1]

    else:
        if symbol < compared:
            return binarySearch(symbol, lines, start, midpoint)
        else:
            return binarySearch(symbol,lines,midpoint,end)


def combineIndices():
    aero = pull('aerospace')
    auto = toDict(pull('automobile'))
    consumerElec = toDict(pull('consumerElectronics'))
    consumerFin = toDict(pull('consumerFinance'))
    defense = toDict(pull('defense'))
    energy = toDict(pull('energy'))
    finance = toDict(pull('finance'))
    grnsolar = toDict(pull('grnsolar'))
    healthCare = toDict(pull('healthCare'))
    industry = toDict(pull('industry'))
    insurance = toDict(pull('insurance'))
    oil = toDict(pull('oil'))
    semi = toDict(pull('semiconductors'))
    smart = toDict(pull('smartphone'))
    soft = toDict(pull('software'))
    tele = toDict(pull('telecommunications'))
    trans = toDict(pull('transportation'))

    destination = open('newIndices','w')
    headers = 'Date, Aerospace, Automobile, Consumer Electronics, Consumer Finance, Defense, Energy, ' +\
              'Finance, GrnSolar, Health Care, Industry, Insurance, Oil, Semiconductors, Smartphones, ' +\
              'Software, Telecommunications, Transportation' + '\n'
    destination.write(headers)


    for record in range(1,len(aero)):
        broken = aero[record].split(',')
        date = broken[0]
        aeroPrice = broken [1]

        try:
            result = date + ', ' + aeroPrice+ ', ' + auto[date].split(',')[1]+ ', ' + consumerElec[date].split(',')[1] + \
                     ', ' + consumerFin[date].split(',')[1] + ', ' + defense[date].split(',')[1] + ', ' +\
                     energy[date].split(',')[1]+ ', ' + finance[date].split(',')[1] + ', ' + grnsolar[date].split(',')[1] +\
                     ', ' + healthCare[date].split(',')[1] + ', ' + industry[date].split(',')[1] + ', ' +\
                     insurance[date].split(',')[1] + ', ' + oil[date].split(',')[1] + ', ' + semi[date].split(',')[1] +\
                     ', ' + smart[date].split(',')[1] + ', ' + soft[date].split(',')[1] + ', ' + tele[date].split(',')[1] + \
                     ', ' + trans[date].split(',')[1] + '\n'
        except KeyError:
            continue

        destination.write(result)





def adding():

    companies = pull('allPrices')
    indices = toDict(pull('newIndices'))
    #gold = toDict(pull('Gold'))
    # ruth = toDict(pull('Ruth'))
    # iron = toDict(pull('Iron'))
    # oil = toDict(pull('oil'))
    # consumer = toDict(pull('Consumer'))
    # software = toDict(pull('software'))

    destination = open('combined_ver_3', 'w')

    for record in companies:

        divided = record.split(',')

        ticker = divided[0]
        recordDate = divided[1]
        recordOpen = divided[2]
        recordClose = divided[5]
        delta = float(recordClose) - float(recordOpen)

        fromIndex = indices.get(recordDate)

        if fromIndex != None:
        #
        #     fromGold = gold.get(recordDate)
        #
        #     if fromGold != None:
        #
        #         fromRuth = ruth.get(recordDate)
        #
        #         if fromRuth != None:
        #
        #             fromIron = iron.get(recordDate)
        #
        #             if fromIron != None:
        #
        #                 fromOil = oil.get(recordDate)
        #
        #                 if fromOil != None:
        #
        #                     fromConsumer = consumer.get(recordDate)
        #
        #                     if fromConsumer != None:
        #
        #                         fromSoft = software.get(recordDate)
        #
        #                         if fromSoft != None:

                                   # record+= ',' + fromIdex + ','+fromGold+','+fromRuth+','+fromIron+','+\
                                             #fromOil+','+fromConsumer+','+fromSoft
                                    boolean = ''
                                    if delta < 0:
                                        boolean= 'False'
                                    else:
                                        boolean= 'True'

                                    result = ticker + ', ' + recordDate + ', ' + recordOpen +\
                                             ', ' + recordClose + ', ' + fromIndex.rstrip() + ', ' + boolean + '\n'


                                    destination.write(result)

        # fromIron = iron.get(recordDate)
        #
        # if fromIron != None:
        #     record+= fromIron
        #
        #     if delta <0:
        #         record+= 'False'
        #     else:
        #         record+= 'True'
        #
        #     destination.write(record)

def toDict(  list ):

    dict = {}

    for line in list:

        parts = line.split(',')

        sep = ','

        dict[ parts[0] ] = sep.join(parts[1:])
    return dict


def formatDate( date ):

    parts = date.split('/')
    if len(parts[0]) < 2:
        parts[0] = '0' + parts[0]
    if len(parts[1]) < 2:
        parts[1] = '0' + parts[1]

    newDate = parts[2] + '-' + parts[0] + '-' + parts[1]
    return newDate





def main():
    #extract()
    adding()
    #combineIndices()

if __name__ == '__main__':
    main()




