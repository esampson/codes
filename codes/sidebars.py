import textwrap

blank = ' ' * 28

def blank_template_block():
    block = []
    blank = ' ' * 28
    for count in range(15):
        block.append(blank)
    return block

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
                                  subentry='temp')) +'/' +
                   str(target.get('Glamour',statclass='Advantage',
                                  subentry='perm')))
        block.append(' Glamour:' + glamour.rjust(18) + ' ')
        clarity = (str(target.get('Clarity',statclass='Advantage',
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
        block.append(
            ' Integrity:' + str(
                target.get('Integrity',statclass='Advantage')).rjust(16) + ' ')
    except:
        for line in range(15):
            block.append(blank)    
    return block

def vampire_template_block(target):
    block = []
    try:
        temp=[]
        entries = ['Clan', 'Covenant', 'Mask', 'Dirge']
        for entry in entries:
            temp.append(' ' + (entry + ":").ljust(14) + 
                         target.get(entry,statclass='Sphere'))
        coterie = target.get('Coterie',statclass='Sphere')
        if coterie and len(coterie) > 0:
            temp.append(' ' + 'Coterie:'.ljust(14) + coterie)
        mystery = target.get('Mystery Coil', statclass='Sphere')
        if mystery and len(mystery) > 0:
            temp.append(' ' + 'Mystery Coil:'.ljust(14) + mystery)
        for line in temp:
            for subline in textwrap.wrap(line,27,subsequent_indent='  '):
                block.append(subline.ljust(28))
        if len(block) < 15:
            for extra in range(len(block),15):
                block.append(blank)
        block[12]=(' Blood Potency:' + str(target.get('Blood Potency',
                        statclass='Power')).rjust(12) + ' ')
        vitae = (str(target.get('Vitae',statclass='Advantage',
                                  subentry='temp')) +'/' +
                   str(target.get('Vitae',statclass='Advantage',
                                  subentry='perm')))
        block[13]=(' Vitae:' + vitae.rjust(20) + ' ')
        humanity = str(target.get('Humanity',statclass='Advantage'))
        block[14]=(' Humanity:' + humanity.rjust(17) + ' ')
    except:
        for line in range(15):
            block.append(blank)
    return block

def werewolf_template_block(target):
    block = []
    try:
        temp=[]
        entries = ['Auspice', 'Tribe', 'Blood', 'Bone']
        for entry in entries:
            temp.append(' ' + (entry + ":").ljust(9) +
                         target.get(entry,statclass='Sphere'))
        pack = target.get('Pack',statclass='Sphere')
        if pack and len(pack) > 0:
            temp.append(' ' + 'Pack:'.ljust(14) + pack)
        for line in temp:
            for subline in textwrap.wrap(line,27,subsequent_indent='  '):
                block.append(subline.ljust(28))
        if len(block) < 15:
            for extra in range(len(block),15):
                block.append(blank)
        block[7] = (' Cunning:' + str(target.get('Cunning',
                                        statclass='Renown')).rjust(18) + ' ')
        block[8] = (' Glory:' + str(target.get('Glory',
                                        statclass='Renown')).rjust(20) + ' ')
        block[9] = (' Honor:' + str(target.get('Honor',
                                        statclass='Renown')).rjust(20) + ' ')
        block[10] = (' Purity:' + str(target.get('Purity',
                                        statclass='Renown')).rjust(19) + ' ')
        block[11] = (' Wisdom:' + str(target.get('Wisdom',
                                        statclass='Renown')).rjust(19) + ' ')
        block[12]=(' Primal Urge:' + str(target.get('Primal Urge',
                                        statclass='Power')).rjust(14) + ' ')
        essence = (str(target.get('Essence',statclass='Advantage',
                                        subentry='temp')) +'/' +
                   str(target.get('Essence',statclass='Advantage',
                                        subentry='perm')))
        block[13]=(' Essence:' + essence.rjust(18) + ' ')
        harmony = str(target.get('Harmony',statclass='Advantage'))
        block[14]=(' Harmony:' +harmony.rjust(18) + ' ')
    except:
        for line in range(15):
            block.append(blank)
    return block
    