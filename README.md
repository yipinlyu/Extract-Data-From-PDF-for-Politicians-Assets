# Webscraping for Politicians Assets

1. Method: 
I use the tabula-py package in Python to extract information from these tables. Please notice that changing the default directory is very important. Otherwise, there might be some errors when importing the tabula package. I use to consult the author of the package about this issue. Moreover, sometimes there is an error because of the missing data. In this case, running the additional code manually.

First, I create a data frame to store this information. Then, I use the tabula package to extract the columns and save them. Please notice that for the other information part, there is some additional transformation because the results differ for different pages. At last, I clean the unnecessary "'" or "?" for financial data and store the data.


2. Columns Discription:
(1) General information
EJERCICIO LEGISLATIVO: Period
DNI / CI: Indentity Number
A. PATERNO: Last Name (Father)
A. MATERNO: Last Name (Mother)
NOMBRES: First Name

(2) Period information
AL INICIO: If "X," at the beginning of the period.

ENTREGA PERIÓDICA: If "X," in the middle of the period
.
AL CESAR:  If "X," at the end of the period


(3)Financial information:

INGRESOS MENSUALES_SECTOR PÚBLICO
INGRESOS MENSUALES_SECTOR PRIVADO
INGRESOS MENSUALES_TOTAL S/.
OTROS *_SECTOR PÚBLICO
OTROS *_SECTOR PRIVADO
OTROS *_TOTAL S/.
BIENES **_SECTOR PÚBLICO
BIENES **_SECTOR PRIVADO
BIENES **_TOTAL S/.

(4) Other information
OTRA INFORMACIÓN QUE CONSIDERE EL OBLIGADO
OTRA INFORMACIÓN_TOTAL S/.

