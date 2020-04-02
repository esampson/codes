from evennia.utils.evmenu import EvMenu
from evennia.utils.utils import m_len, pad
from evennia.utils.ansi import strip_ansi
from django.conf import settings
from evennia.utils.evtable import EvTable

# read from protocol NAWS later?
_MAX_TEXT_WIDTH = settings.CLIENT_DEFAULT_WIDTH     

class XPMenu(EvMenu):
    
    pass
    
    def options_formatter(self, optionlist):
        """
        Formats the option block.
 
        Args:
            optionlist (list): List of (key, description) tuples for every
                option related to this node.
            caller (Object, Account or None, optional): The caller of the node.
 
        Returns:
            options (str): The formatted option display.
 
        """
        if not optionlist:
            return ""
 
        # column separation distance
        colsep = 4
        option_list_1 = []
        option_list_2 = []
        for item in optionlist:
            if item[0].lower() in ['q','b','p']:
                option_list_2.append(item)
            else:
                option_list_1.append(item)
        nlist = len(option_list_1)
 
        # get the widest option line in the table.
        table_width_max = -1
        table = []
        for key, desc in option_list_1:
            if key or desc:
                desc_string = ": %s" % desc if desc else ""
                table_width_max = max(
                    table_width_max,
                    max(m_len(p) for p in key.split("\n"))
                    + max(m_len(p) for p in desc_string.split("\n"))
                    + colsep,
                )
                raw_key = strip_ansi(key)
                if raw_key != key:
                    # already decorations in key definition
                    table.append(" |lc%s|lt%s|le%s" % (raw_key, key, desc_string))
                else:
                    # add a default white color to key
                    table.append(" |lc%s|lt|w%s|n|le%s" % (raw_key, raw_key, desc_string))
        ncols = _MAX_TEXT_WIDTH // table_width_max  # number of ncols
 
        if ncols < 0:
            # no visible option at all
            return ""
 
        ncols = ncols + 1 if ncols == 0 else ncols
        # get the amount of rows needed (start with 4 rows)
        nrows = 4
        while nrows * ncols < nlist:
            nrows += 1
        ncols = nlist // nrows  # number of full columns
        nlastcol = nlist % nrows  # number of elements in last column
 
        # get the final column count
        ncols = ncols + 1 if nlastcol > 0 else ncols
        if ncols > 1:
            # only extend if longer than one column
            table.extend([" " for i in range(nrows - nlastcol)])
 
        # build the actual table grid
        table = [table[icol * nrows : (icol * nrows) + nrows] for icol in range(0, ncols)]
 
        # adjust the width of each column
        for icol in range(len(table)):
            col_width = (
                max(max(m_len(p) for p in part.split("\n")) for part in table[icol]) + colsep
            )
            table[icol] = [pad(part, width=col_width + colsep, align="l") for part in table[icol]]
        result = EvTable(table=table, border='none')
        result.add_row(' ')
        for key, desc in option_list_2:
            if key or desc:
                desc_string = ": %s" % desc if desc else ""
                table_width_max = max(
                    table_width_max,
                    max(m_len(p) for p in key.split("\n"))
                    + max(m_len(p) for p in desc_string.split("\n"))
                    + colsep,
                )
                raw_key = strip_ansi(key)
                if raw_key != key:
                    # already decorations in key definition
                    result.add_row(" |lc%s|lt%s|le%s" % (raw_key, key, desc_string))
                else:
                    # add a default white color to key
                    result.add_row(" |lc%s|lt|w%s|n|le%s" % (raw_key, raw_key, desc_string))
 
        # format the table into columns
        return str(result)
    
    def node_formatter(self, nodetext, optionstext):
        """
        Formats the entirety of the node.

        Args:
            nodetext (str): The node text as returned by `self.nodetext_formatter`.
            optionstext (str): The options display as returned by `self.options_formatter`.
            caller (Object, Account or None, optional): The caller of the node.

        Returns:
            node (str): The formatted node to display.

        """
        sep = '-'

        if self._session:
            screen_width = self._session.protocol_flags.get("SCREENWIDTH", {0: _MAX_TEXT_WIDTH})[0]
        else:
            screen_width = _MAX_TEXT_WIDTH

        nodetext_width_max = max(m_len(line) for line in nodetext.split("\n"))
        options_width_max = max(m_len(line) for line in optionstext.split("\n"))
        total_width = min(screen_width, max(options_width_max, nodetext_width_max))
        separator1 = '_' * total_width + "\n\n" if nodetext_width_max else ""
        separator2 = "\n" + '_' * total_width + "\n\n" if total_width else ""
        separator3 = "\n" 
        separator4 = "\n" + sep * total_width + "\n" if total_width else ""
        if len(nodetext) < 20:
            result = separator3 + "|n" + nodetext + "|n\n" + optionstext
        else:
            result = separator1 + "|n" + nodetext + "|n" + separator2 + "|n" + optionstext
        return result
    
    