from openpyxl import load_workbook
import csv

def toBinary( filename ):
    """
    Converts numeric CSV files to a binary CSV file
    where each attribute is either true or false
    :param filename: the file to convert
    :return: Nothing
    """

    lines = None

    with open('../Individual Company Data/' + filename + '.csv') as file:
        lines = file.readlines()

    destination = open('../Individual Company Data/Binary' + filename + '.csv', 'w')

    # Write attribute names
    destination.write(lines[0])

    # Initialize first row to False
    firstRow = lines[1].split(',')
    destination.write(firstRow[0] + ', ' + firstRow[1] + ', ')
    for i in range(2,len(firstRow)-1):
        destination.write('False, ')
    destination.write('False' + '\n')

    previousRow = firstRow
    currentRow = lines[2].split(',')

    # Convert remaining rows
    for j in range(2,len(lines)):

        destination.write(currentRow[0]+', '+currentRow[1]+', ')

        # Convert attributes
        for a in range(2,len(currentRow)-1):

            previousValue = float(previousRow[a])
            currentValue = float(currentRow[a])

            if currentValue - previousValue < 0:
                destination.write('False, ')
            else:
                destination.write('True, ')

        destination.write(currentRow[len(currentRow)-1])

        # Update previous row
        previousRow = currentRow

        # If we have not reached the end, update
        # current row
        if j < len(lines)-1:
            currentRow = lines[j+1].split(',')


def main():

    companies = 'APPL,ADBE,ADI,ADP,ADSK,AMAT,AMD,CA,CERN,CRM,CSC,CSCO,CTSH,CTXS,CVG,DOV,ETN,FISV,FSLR,GOOG,HPQ,IBM,INTC' +\
        ',INTU,IPG,ITW,JBL,JNPR,LLL,LLTC,MCHP,MSFT,MU,NTAP,NVDA,OMC,ORCL,QCOM,RHT,RHI,SYMC,TDC,TXN,VRSN,WDC,XLNX,YHOO'
    companiesList = companies.split(',')

    for company in companiesList:
        path = '../Individual Company Data/' + company + '.xlsx'
        wb = load_workbook(path)
        ws = wb.active
        with open('../Individual Company Data/' + company + '.csv', 'w',newline='' ) as f:
            c = csv.writer(f)
            for row in ws.rows:
               # print(row)
                c.writerow([cell.value for cell in row])
        toBinary(company)

if __name__ == '__main__':
    main()








