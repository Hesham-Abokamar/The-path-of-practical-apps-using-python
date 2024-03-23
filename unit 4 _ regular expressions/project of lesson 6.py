import re

txt = "استئناف-رفع-الملفات-بعد-فقدان-الاتصال-في-جافاسكريبت"

replace = re.sub('-', ' ', txt)
print(replace)