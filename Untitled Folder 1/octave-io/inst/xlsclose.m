## Copyright (C) 2009-2018 Philip Nienhuis
##
## This program is free software; you can redistribute it and/or modify it under
## the terms of the GNU General Public License as published by the Free Software
## Foundation; either version 3 of the License, or (at your option) any later
## version.
##
## This program is distributed in the hope that it will be useful, but WITHOUT
## ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
## FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
## details.
##
## You should have received a copy of the GNU General Public License along with
## this program; if not, see <http://www.gnu.org/licenses/>.

## -*- texinfo -*-
## @deftypefn {Function File} [@var{xls}] = xlsclose (@var{xls})
## @deftypefnx {Function File} [@var{xls}] = xlsclose (@var{xls}, @var{filename})
## @deftypefnx {Function File} [@var{xls}] = xlsclose (@var{xls}, "FORCE")
## Close the Excel spreadsheet pointed to in struct @var{xls}, if needed
## write the file to disk.  Based on information contained in @var{xls},
## xlsclose will determine if the file should be written to disk.
##
## If no errors occured during writing, the xls file pointer struct will be
## reset and -if COM interface was used- ActiveX/Excel will be closed.
## However if errors occurred, the file pointer will be untouched so you can
## clean up before a next try with xlsclose().
## Be warned that until xlsopen is called again with the same @var{xls} pointer
## struct, hidden Excel or Java applications with associated (possibly large)
## memory chunks are kept in memory, taking up resources.
## If (string) argument "FORCE" is supplied, the file pointer will be reset 
## regardless, whether the possibly modified file has been saved successfully
## or not.  Hidden Excel (COM) or OpenOffice.org (UNO) invocations may live on,
## possibly even impeding proper shutdown of Octave.
##
## @var{filename} can be used to write changed spreadsheet files to
## an other file than opened with xlsopen(); unfortunately this doesn't work
## with JXL (JExcelAPI) interface.
##
## For other file formats than OOXML, ODS or gnumeric, you need MS-Excel
## (95 - 2010), and/or the Java package => 1.2.8 plus Apache POI > 3.5 and/or
## JExcelAPI and/or OpenXLS and/or OpenOffice.org or clones installed on your
## computer + proper javaclasspath set, to make this function work at all.
## For Octave >= 3.8.0 the Java package isn't needed as Java support should
## be built-in.
##
## @var{xls} must be a valid pointer struct made by xlsopen() in the same
## octave session.
##
## Examples:
##
## @example
##   xls1 = xlsclose (xls1);
##   (Close spreadsheet file pointed to in pointer struct xls1; xls1 is reset)
## @end example
##
## @seealso {xlsopen, xlsread, xlswrite, xls2oct, oct2xls, xlsfinfo}
##
## @end deftypefn

## Author: Philip Nienhuis <prnienhuis at users.sf.net>
## Created: 2009-11-29

function [ xls ] = xlsclose (xls, varargin)

  if (isempty (xls))
    warning ("xlsclose: file pointer struct was already closed\n");
    return
  endif

  force = 0;

  if (nargin > 1)
    for ii=1:nargin-1
      if (strcmpi (varargin{ii}, "force"))
        ## Close .xls anyway even if write errors occur
        force = 1;

      ## Interface-specific clauses here:
      elseif (! isempty (strfind (tolower (varargin{ii}), ".")))
        ## Apparently a file name. First some checks....
        if (xls.changed == 0 || xls.changed > 2)
          warning ("xlsclose: file %s wasn't changed, new filename ignored.\n", xls.filename);
        elseif (strcmp (xls.xtype, "JXL"))
          error ("xlsclose: JXL doesn't support changing filename, new filename ignored.\n");
        elseif (isempty (strfind ( lower (varargin{ii}), ".xls")) && ...
                (! (strcmp (xls.xtype, "COM") || strcmp (xls.xtype, "UNO"))))
          # Excel/ActiveX && OOo (UNO bridge) will write any valid filetype; POI/JXL/OXS need .xls[x]
          error ("xlsclose: .xls or .xlsx suffix lacking in filename %s\n", varargin{ii});
        else
          ## For multi-user environments, uncomment below AND relevant stanza in xlsopen
          ## In case of COM, be sure to first close the open workbook
          ##if (strcmp (xls.xtype, 'COM'))
          ##   xls.app.Application.DisplayAlerts = 0;
          ##   xls.workbook.close();
          ##   xls.app.Application.DisplayAlerts = 0;
          ##endif
          ## Preprocessing / -checking ready. Assign filename arg to file ptr struct
          xls.nfilename = varargin{ii};
        endif
      endif
    endfor
  endif

  if (strcmp (xls.xtype, "COM"))
    xls = __COM_spsh_close__ (xls);

  elseif (strcmp (xls.xtype, "POI"))
    xls = __POI_spsh_close__ (xls);

  elseif (strcmp (xls.xtype, "JXL"))
    xls = __JXL_spsh_close__ (xls);

  elseif (strcmp (xls.xtype, "OXS"))
    xls = __OXS_spsh_close__ (xls);

  elseif (strcmp (xls.xtype, "UNO"))
    xls = __UNO_spsh_close__ (xls, force);

  elseif (strcmp (xls.xtype, "OCT"))
    xls = __OCT_spsh_close__ (xls, "xlsclose");

  ## elseif   <other interfaces here>

  endif

  if (xls.changed && xls.changed < 3)
    warning (sprintf ("xlsclose: file %s could not be saved. Read-only or in use elsewhere?\n", ...
                      xls.filename));
    if (force)
      xls = [];
    else
      printf ("(File pointer preserved. Try saving again later...)\n");
    endif
  else
    xls = [];
  endif

endfunction
