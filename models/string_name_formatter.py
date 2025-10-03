from typing import Dict


class StringNameFormatter:
    @staticmethod
    def create_unique_string_names(note_octave_pairs: list) -> Dict[str, str]:
        new_strings = {}
        used_names = {}
        total_strings = len(note_octave_pairs)

        for i, (note, octave) in enumerate(note_octave_pairs):
            base_name = f"{note}{octave}"
            internal_name = StringNameFormatter._generate_internal_name(base_name, i, total_strings, used_names)
            new_strings[internal_name] = base_name

        return new_strings

    @staticmethod
    def _generate_internal_name(base_name: str, index: int, total: int, used_names: Dict[str, int]) -> str:
        string_number = index + 1

        if base_name in used_names:
            used_names[base_name] += 1
            return f"String{string_number}_{base_name}_{used_names[base_name]}"

        used_names[base_name] = 0

        if total == 1:
            return f"String1_{base_name}"

        if index == 0:
            return f"String1_{base_name}_Low"

        if index == total - 1:
            return f"String{total}_{base_name}_High"

        return f"String{string_number}_{base_name}"
    
    @staticmethod
    def get_display_name(internal_name: str) -> str:
        if not internal_name.startswith("String"):
            return internal_name

        parts = internal_name.split("_")

        if len(parts) < 2:
            return internal_name

        note = parts[1]

        if len(parts) >= 3 and parts[2] == "Low":
            return f"{note} (Low)"

        if len(parts) >= 3 and parts[2] == "High":
            return f"{note} (High)"

        return note