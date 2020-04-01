import textwrap

blank = ' ' * 28

def changeling_template_block(target):
    block = []
    try:
        regalia = target.get('Regalia',statclass='Sphere')
        entries = ['Seeming', 'Kith', 'Court', 'Needle', 'Thread']
        for entry in entries:
            block.append(' ' + (entry + ":").ljust(9) + 
                         target.get(entry,statclass='Sphere').ljust(18))
        block.append(' Regalia: ' + 
                     (regalia[0] + ' & ' + regalia[1]).ljust(18))
        motley = target.get('Motley',statclass='Sphere')
        if motley and len(motley) > 0:
            motley_list = [' Motley:                    ']
            for line in textwrap.wrap(motley,25):
                motley_list.append('  ' + line.ljust(25) + ' ')
            list_length = len(motley_list)
        else:
            motley_list=[]
            list_length = 0
        entitlement = target.get('Entitlement',statclass='Sphere')
        if entitlement and len(entitlement) > 0:
            entitlement_list = [' Entitlement:               ']
            for line in textwrap.wrap(entitlement,25):
                entitlement_list.append('  ' + line.ljust(25) + ' ')
            list_length = list_length + len(entitlement_list)
        else:
            entitlement_list = []
        if list_length >= 6 and len(entitlement_list) == 0:
            for line in range(6):
                block.append(motley_list[line])
        elif list_length >= 6 and len(motley_list) == 0:
            for line in range(6):
                block.append(entitlement_list[line])
        elif list_length > 6 and len(entitlement_list) == 1:
            for line in range(4):
                block.append(motley_list[line])
            block.append(entitlement_list[0])
            block.append(entitlement_list[1])
        elif list_length > 6 and len(motley_list) == 1:
            block.append(motley_list[0])
            block.append(motley_list[1])
            for line in range(4):
                block.append(entitlement_list[line])
        elif list_length > 6:
            for line in range(3):
                block.append(motley_list[line])
            for line in range(3):
                block.append(entitlement_list[line])
        else:
            for line in motley_list:
                block.append(line)
            for line in entitlement_list:
                block.append(line)
            for line in range((list_length),6):
                block.append('                            ')
        block.append(' Wyrd:' + str(target.get('Wyrd',
                        statclass='Power')).rjust(21) + ' ')
        glamour = (str(target.get('Glamour',statclass='Advantage',
                                  subentry='perm') -
                       target.get('Glamour',statclass='Advantage',
                                  subentry='temp')) +'/' +
                   str(target.get('Glamour',statclass='Advantage',
                                  subentry='perm')))
        block.append(' Glamour:' + glamour.rjust(18) + ' ')
        clarity = (str(target.get('Clarity',statclass='Advantage',
                                  subentry='perm') -
                       target.get('Clarity',statclass='Advantage',
                                  subentry='temp')) +'/' +
                   str(target.get('Clarity',statclass='Advantage',
                                  subentry='perm')))
        block.append(' Clarity:' + clarity.rjust(18) + ' ')
    except:
        for line in range(15):
            block.append(blank)
    return block

def mortal_template_block(target):
    block = []
    try:
        entries = ['Virtue', 'Vice']
        for entry in entries:
            block.append(' ' + (entry + ":").ljust(9) + 
                         target.get(entry ,statclass='Sphere').ljust(18))
        for line in range(12):
            block.append('                            ')
        block.append(' Integrity:' + str(target.get('Integrity',statclass='Advantage')).rjust(16) + ' ')
    except:
        for line in range(15):
            block.append(blank)    
    return block
    