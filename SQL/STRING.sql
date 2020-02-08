SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ("Lucy", "Ella", "Pickle", "Rogan", "Sabrina", "Mitty")


SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE ANIMAL_TYPE = "Dog" and
    (NAME LIKE "El%" OR
    NAME LIKE "%el%" OR 
    NAME LIKE "%el")
ORDER BY NAME


SELECT ANIMAL_ID, NAME, 
CASE WHEN SEX_UPON_INTAKE LIKE "Spayed%" OR 
	SEX_UPON_INTAKE LIKE "Neutered%" THEN "O" ELSE "X" END AS 중성화
FROM ANIMAL_INS
ORDER BY ANIMAL_ID