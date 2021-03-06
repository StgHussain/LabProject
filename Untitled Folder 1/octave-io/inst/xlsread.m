## Copyright (C) 2009-2018 by Philip Nienhuis
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
## @deftypefn {Function File} [@var{numarr}, @var{txtarr}, @var{rawarr},  @var{limits}] = xlsread (@var{filename})
## @deftypefnx {Function File} [@var{numarr}, @var{txtarr}, @var{rawarr}, @var{limits}] = xlsread (@var{filename}, @var{wsh})
## @deftypefnx {Function File} [@var{numarr}, @var{txtarr}, @var{rawarr}, @var{limits}] = xlsread (@var{filename}, @var{range})
## @deftypefnx {Function File} [@var{numarr}, @var{txtarr}, @var{rawarr}, @var{limits}] = xlsread (@var{filename}, @var{wsh}, @var{range})
## @deftypefnx {Function File} [@var{numarr}, @var{txtarr}, @var{rawarr}, @var{limits}, @var{extout}] = xlsread (@var{filename}, @var{wsh}, @var{range}, @var{options}, @dots{})
##
## Read data contained in range @var{range} from worksheet @var{wsh}
## in Excel spreadsheet file @var{filename}. Gnumeric files can also
## be read.
##
## Return argument @var{numarr} contains the numeric data, optional
## return arguments @var{txtarr} and @var{rawarr} contain text strings
## and the raw spreadsheet cell data, respectively.  Return argument
## @var{limits} contains the outer column/row numbers of the read
## spreadsheet range where @var{numarr}, @var{txtarr} and @var{rawarr}
## have come from (remember, xlsread trims outer rows and columns).
##
## If @var{filename} does not contain any directory, the file is
## assumed to be in the current directory.  The filename extension
## (.xls or .xlsx) must be included in the file name; when using the
## COM interface all file formats can be read that are supported by the
## locally installed MS-Excel version (e.g., wk1, csv, dbf, .xlsm, etc.).
## The same holds for UNO (OpenOffice.org or LibreOffice).
##
## @var{range} is expected to be a regular spreadsheet range format,
## or "" (empty string, indicating all data in a worksheet).
## If no range is specified the occupied cell range will have to be
## determined behind the scenes first; this can take some time for the
## Java-based interfaces (but the results may be more reliable than
## that of ActiveX/COM).  Instead of a spreadsheet range a Named range
## defined in the spreadsheet file can be used as well. In that case
## the Named range should be specified as 3rd argument and the value
## of 2nd argument @var{wsh} doesn't matter as the worksheet associated
## with the specified Named range will be used.
##
## @var{wsh} is either numerical or text; in the latter case it is 
## case-sensitive and it may be max. 31 characters long.
## Note that in case of a numerical @var{wsh} this number refers to the
## position in the visible sheet stack, counted from the left in a
## spreadsheet program window.  The default is numerical 1, i.e.
## corresponding to the leftmost sheet tab in the spreadsheet file.
##
## If only the first argument is specified, xlsread will try to read
## all contents (as if a range of @'' (empty string) was specified)
## from the first = leftmost (or the only) worksheet
## 
## If only two arguments are specified, xlsread assumes the second
## argument to be @var{range} if it is a string argument and contains 
##  a ":" or if it is @'' (empty string), and in those cases assumes
## the data must be read from the first worksheet (not necessarily
## Sheet1! but the leftmost sheet).
##
## However, if only two arguments are specified and the second argument
## is numeric or a text string that does not contain a ":", it is
## assumed to be @var{wsh} and to refer to a worksheet.  In that case
## xlsread tries to read all data contained in that worksheet.
## 
## To be able to use Named ranges, the second input argument should
## refer to a worksheet and the third should be the Named range.
##
## After these input arguments a number of optional arguments can be
## supplied in any desired order:
##
## @table @asis
## @item @var{Interface}
## @var{Interface} (a three-character text sting) can be used to override
## the automatic interface selection by xlsread out of the supported
## ones: COM/Excel, Java/Apache POI, Java/JExcelAPI, Java/OpenXLS,
## Java/UNO (OpenOffice.org), or native Octave (in that -built in-
## order of preference).
## For I/O to/from .xlsx files a value of 'com', 'poi', 'uno', or 'oct'
## must be specified for @var{reqintf} (see help for xlsopen).  For
## Excel'95 files use 'com', or if Excel is not installed use 'jxl',
## 'basic' or 'uno'. POI can't read Excel'95 but will try to fall back
## to JXL.  As @var{reqintf} can also be a cell array of strings, one
## can select or exclude one or more interfaces.
## In addition the OCT interface offers .gnumeric read support.
## @end item
##
## @item Function handle
## If a function handle is specified, the pertinent function (having at
## most two output arrays) will be applied to the numeric output data of
## xlsread. Any second output of the function will be in a 5th output
## argument @var{extout} of xlsread.
## @end item
##
## @item Options struct
## xlsread's output can be influenced to some extent by a number of
## options. See OPTIONS in "help xls2oct" for an overview.
## @end item
## @end table
##
## Erroneous data and empty cells are set to NaN in @var{numarr} and
## turn up empty in @var{txtarr} and @var{rawarr}.  Date/time values in
## Excel are returned as numerical values in @var{numarr}.  Note that
## Excel and Octave have different date base values (epoch; 1/1/1900 & 
## 1/1/0000, resp.).  When using the COM interface, spreadsheet date
## values lying before 1/1/1900 are returned as strings, formatted as
## they appear in the spreadsheet.  The returned date format for other
## interfaces depend on interface type and support SW version.
## @var{numarr} and @var{txtarr} are trimmed from empty outer rows
## and columns.  Be aware that Excel does the same for @var{rawarr}, 
## so any returned array may turn out to be smaller than requested in
## @var{range}.  Use the fourth return argument @var{LIMS} for info on the
## cell ranges your date came from.
##
## When reading from merged cells, all array elements NOT corresponding 
## to the leftmost or upper Excel cell will be treated as if the
## "corresponding" Excel cells are empty.
##
## xlsread is just a wrapper for a collection of scripts that find out
## the interface to be used (COM, Java/POI, Java/JXL Java/OXS, Java/UNO,
## OCT) and do the actual reading.  For each call to xlsread the interface
## must be started and the Excel file read into memory.  When reading
## multiple ranges (in optionally multiple worksheets) a significant speed
## boost can be obtained by invoking those scripts directly as in:
## xlsopen / xls2oct [/ parsecell] / ... / xlsclose
##
## Beware: when using the COM interface, hidden Excel invocations may be
## kept running silently if not closed explicitly.
##
## Examples:
##
## @example
##   A = xlsread ('test4.xls', '2nd_sheet', 'C3:AB40');
##   (which returns the numeric contents in range C3:AB40 in worksheet
##   '2nd_sheet' from file test4.xls into numeric array A) 
## @end example
##
## @example
##   [An, Tn, Ra, limits] = xlsread ('Sales2009.xls', 'Third_sheet');
##   (which returns all data in worksheet 'Third_sheet' in file 'Sales2009.xls'
##   into array An, the text data into array Tn, the raw cell data into
##   cell array Ra and the ranges from where the actual data came in limits)
## @end example
##
## @example
##   numarr = xlsread ('Sales2010.xls', 4, [], @{'JXL', 'COM'@});
##   (Read all data from 4th worksheet in file Sales2010.xls using either JXL
##    or COM interface (i.e, exclude POI interface). 
## @end example
##
## @seealso {xlswrite, xlsopen, xls2oct, xlsclose, xlsfinfo, oct2xls}
##
## @end deftypefn

## Author: Philip Nienhuis <prnienhuis at users.sf.net>
## Created: 2009-10-16

function [ numarr, txtarr, rawarr, lims, extout ] = xlsread (fn, wsh, datrange, varargin)

  rstatus = 0;

  if (nargin < 1) 
    error ("xlsread: no input arguments specified\n") 
    numarr = []; txtarr={}; rawarr = {};
    return
  elseif (! ischar (fn))
    error ("filename (text string) expected for argument #1, not a %s\n", class (fn));
  elseif (nargin == 1)
    wsh = 1;
    datrange = ""; 
  elseif (nargin == 2)
    ## Find out whether 2nd argument = worksheet or range
    if (isnumeric (wsh) || (isempty (findstr (wsh, ":" )) && ~isempty (wsh)))
      ## Apparently a worksheet specified
      datrange = "";
    else
      ## Range specified
      datrange = wsh;
      wsh = 1;
    endif
  endif
  reqintf = hndl = opts = extout = [];

  if (nargin > 3)
    for ii=1:nargin-3
      if (ischar (varargin{ii}))
        ## Request a certain interface
        reqintf = varargin{ii};
        ## A small gesture for Matlab compatibility. JExcelAPI supports BIFF5.
        if (! isempty (reqintf) && ischar (reqintf) && strcmpi (reqintf, "BASIC")) 
          reqintf = {"JXL"}; 
          printf ("(BASIC (BIFF5) support request translated to JXL)\n");
        endif
      elseif (strcmp (class (varargin{ii}), "function_handle"))
        ## Function handle to apply to output "num"
        hndl = varargin{ii};
      elseif (isstruct (varargin{ii}))
        ## Various spreadsheet output options
        opts = varargin{ii};
      else
        error ("xlsread: illegal input arg. #%d", ii);
      endif
    endfor
  endif

  ## Checks done. First check for .csv as that doesn't need xlsopen etc;
  ## a convenience for lazy Matlab users (see bugs #40993 & #44511):
  [~, ~, ext] = fileparts (fn);
  if strcmpi (ext, ".csv")
    if (isempty (datrange))
      numarr = dlmread (fn, ",");
    else
      numarr = dlmread (fn, ",", datrange);
    endif
    txtarr = rawarr = lims = [];
    return

  else
    ## Get raw data into cell array "rawarr". xlsopen finds out what interface
    ## to use. If none found, just return as xlsopen will complain enough.
    unwind_protect  ## Needed to catch COM errors & able to close stray Excel
                    ## invocations
      ## Get pointer array to spreadsheet file
      xls_ok = 0;
      xls = xlsopen (fn, 0, reqintf);
      if (! isempty (xls))
        xls_ok = 1;
 
        ## Get data from spreadsheet file & return handle
        [rawarr, xls, rstatus] = xls2oct (xls, wsh, datrange, opts);

        ## Save some results before xls is wiped
        rawlimits = xls.limits;
        xtype = xls.xtype;

        if (rstatus)
          [numarr, txtarr, lims] = parsecell (rawarr, rawlimits);
          if (! isempty (hndl) && ! isempty (numarr))
            try
              [numarr, extout] = feval (hndl, numarr);
            catch
              warning ("xlsread: applying specified function handle failed with:\
error\n'%s'\n", lasterr);
            end_try_catch
          endif
        else
          rawarr = {}; numarr = []; txtarr = {}; extout = [];
        endif
      endif

    unwind_protect_cleanup  
      ## Close Excel file
      if (xls_ok)
        xls = xlsclose (xls);
      endif

    end_unwind_protect
  endif

endfunction
