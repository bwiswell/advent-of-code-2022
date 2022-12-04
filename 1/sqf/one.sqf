_text = loadFile "input.txt";
_lines = _text splitString "\n";

_elfs = [];
_elf = 0;
for "_i" from 0 to (count _lines - 1) do {
	_line = trim (_lines select _i);
	if (count _line > 0) then {
		_elf = _elf + (parseNumber _line);
	} else {
		_elfs pushBack _elf;
		_elf = 0;
	};
};
_elfs sort false;

["TaskSucceeded", ["Top Elf", str (_elfs select 0)]] call BIS_fnc_showNotification;
_three = 0;
for "_i" from 0 to 2 do {
	_three = _three + (_elfs select _i);
};
["TaskSucceeded", ["Top Elfs", str _three]] call BIS_fnc_showNotification;