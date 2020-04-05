from evennia.utils.evmenu import EvMenu
from evennia.utils.utils import m_len, pad
from evennia.utils.ansi import strip_ansi
from django.conf import settings
from evennia.utils.evtable import EvTable
from evennia.utils.utils import strip_control_sequences, make_iter

from django.utils.translation import gettext as _

# read from protocol NAWS later?
_MAX_TEXT_WIDTH = settings.CLIENT_DEFAULT_WIDTH

_HELP_FULL = _("Commands: <menu option>, help, quit")
_HELP_NO_QUIT = _("Commands: <menu option>, help")
_HELP_NO_OPTIONS = _("Commands: help, quit")
_HELP_NO_OPTIONS_NO_QUIT = _("Commands: help")
_HELP_NO_OPTION_MATCH = _("Choose an option or try 'help'.")

class ExMenu(EvMenu):
    
    pass
    
    def nodetext_formatter(self, nodetext):
        """
        Format the node text itself.
        Args:
            nodetext (str): The full node text (the text describing the node).
        Returns:
            nodetext (str): The formatted node text.
        """
        if type(nodetext) == str:
            nodetext = nodetext.strip("\n").rstrip()
        elif type(nodetext) == dict:
            if 'text' in nodetext:
                nodetext['text'] = nodetext['text'].strip("\n").rstrip()
        return nodetext
    
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
        
        # parse out options for Quit, Back, Proceed, None, and Finish
        option_list_1 = []
        option_list_2 = []
        for item in optionlist:
            if (item[0].lower() in ['q', 'b', 'p', 'f'] or 
                    (item[1].lower() in ['none'] and item[0].lower() == 'n')):
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
        if len(option_list_2) > 0:
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
        
        if type(nodetext) == dict:
            if 'text' in nodetext:
                text = nodetext['text']
            else:
                text = ''
            if 'format' in nodetext:
                args = nodetext['format']
            else:
                args=''
        else:
            text = str(nodetext)
            args = ''

        if self._session:
            screen_width = self._session.protocol_flags.get("SCREENWIDTH", {0: _MAX_TEXT_WIDTH})[0]
        else:
            screen_width = _MAX_TEXT_WIDTH

        nodetext_width_max = max(m_len(line) for line in text.split("\n"))
        options_width_max = max(m_len(line) for line in optionstext.split("\n"))
        total_width = min(screen_width, max(options_width_max, nodetext_width_max))
        separator1 = '_' * total_width + "\n\n" if nodetext_width_max else ""
        separator2 = "\n" + '_' * total_width + "\n\n" if total_width else ""
        if args == 'suppress':
            result = 'Trying to really be quiet'
        elif args == 'no_bars':
            result = text + "|n\n" + optionstext
        else:
            result = separator1 + "|n" + text + "|n" + separator2 + "|n" + optionstext
        return result
    
    def display_nodetext(self):
        if self.nodetext != 'Trying to really be quiet':
            self.caller.msg(self.nodetext)
            
    def goto(self, nodename, raw_string, **kwargs):
        """
        Run a node by name, optionally dynamically generating that name first.
        Args:
            nodename (str or callable): Name of node or a callable
                to be called as `function(caller, raw_string, **kwargs)` or
                `function(caller, **kwargs)` to return the actual goto string or
                a ("nodename", kwargs) tuple.
            raw_string (str): The raw default string entered on the
                previous node (only used if the node accepts it as an
                argument)
        Kwargs:
            any: Extra arguments to goto callables.
        """

        if callable(nodename):
            # run the "goto" callable, if possible
            inp_nodename = nodename
            nodename = self._safe_call(nodename, raw_string, **kwargs)
            if isinstance(nodename, (tuple, list)):
                if not len(nodename) > 1 or not isinstance(nodename[1], dict):
                    raise EvMenuError(
                        "{}: goto callable must return str or (str, dict)".format(inp_nodename)
                    )
                nodename, kwargs = nodename[:2]
            if not nodename:
                # no nodename return. Re-run current node
                nodename = self.nodename
        try:
            # execute the found node, make use of the returns.
            nodetext, options = self._execute_node(nodename, raw_string, **kwargs)
        except EvMenuError:
            return

        if self._persistent:
            self.caller.attributes.add(
                "_menutree_saved_startnode", (nodename, (raw_string, kwargs))
            )

        # validation of the node return values
        helptext = ""
        if type(nodetext) == dict:
            if 'help' in nodetext:
                helptext = nodetext['help']
        nodetext = "" if nodetext is None else nodetext
        options = [options] if isinstance(options, dict) else options

        # this will be displayed in the given order
        display_options = []
        # this is used for lookup
        self.options = {}
        self.default = None
        if options:
            for inum, dic in enumerate(options):
                # fix up the option dicts
                keys = make_iter(dic.get("key"))
                desc = dic.get("desc", dic.get("text", None))
                if "_default" in keys:
                    keys = [key for key in keys if key != "_default"]
                    goto, goto_kwargs, execute, exec_kwargs = self.extract_goto_exec(nodename, dic)
                    self.default = (goto, goto_kwargs, execute, exec_kwargs)
                else:
                    # use the key (only) if set, otherwise use the running number
                    keys = list(make_iter(dic.get("key", str(inum + 1).strip())))
                    goto, goto_kwargs, execute, exec_kwargs = self.extract_goto_exec(nodename, dic)
                if keys:
                    display_options.append((keys[0], desc))
                    for key in keys:
                        if goto or execute:
                            self.options[strip_ansi(key).strip().lower()] = (
                                goto,
                                goto_kwargs,
                                execute,
                                exec_kwargs,
                            )

        self.nodetext = self._format_node(nodetext, display_options)
        self.node_kwargs = kwargs
        self.nodename = nodename

        # handle the helptext
        if helptext:
            self.helptext = self.helptext_formatter(helptext)
        elif options:
            self.helptext = _HELP_FULL if self.auto_quit else _HELP_NO_QUIT
        else:
            self.helptext = _HELP_NO_OPTIONS if self.auto_quit else _HELP_NO_OPTIONS_NO_QUIT

        self.display_nodetext()
        if not options:
            self.close_menu()
    