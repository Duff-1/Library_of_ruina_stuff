BEGIN palendromefinder

    LET endword = 'zzz'
    LET line = ''
    LET words = []
    OPEN words.txt

    WHILE line != endword DO
        index = 1
        line = words.txt[index]
        LET words[index] = line
    ENDWHILE

    CLOSE words.txt

    FOR word = 1 length of words STEP 1
        check = isPalendrome(word)
        IF check == TRUE
            DISPLAY word
        ENDIF
    NEXT word

END

BEGIN isPalendrome(word)

    FOR char = length(word) IN word STEP -1

    NEXT char


END