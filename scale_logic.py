notes_sharp = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
notes_flat = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
scale_intervals = {
    "major": [2, 2, 1, 2, 2, 2, 1],
    "minor": [2, 1, 2, 2, 1, 2, 2],
    "dorian": [2, 1, 2, 2, 2, 1, 2],
    "phrygian": [1, 2, 2, 2, 1, 2, 2],
    "lydian": [2, 2, 2, 1, 2, 2, 1],
    "mixolydian": [2, 2, 1, 2, 2, 1, 2],
    "locrian": [1, 2, 2, 1, 2, 2, 2],
    "harmonic_minor": [2, 1, 2, 2, 1, 3, 1],
    "melodic_minor": [2, 1, 2, 2, 2, 2, 1],
}     

def generate_scale(root, scale_type):
    notes = notes_sharp

    try:
        start_index = notes.index(root)
    except ValueError:
        return f"Error: '{root}' is not a valid note."
    
    intervals = scale_intervals.get(scale_type.lower())
    if not intervals:
        return f"Error: '{scale_type}' is not a supported scale."
    
    scale = [root]
    current_index = start_index

    for step in intervals[:-1]:
        current_index = (current_index + step) % len(notes)
        scale.append(notes[current_index])

    return scale

if __name__ == "__main__":
    # Test a few different scales
    print(f"C Major: {generate_scale('C', 'major')}")
    print(f"A Minor: {generate_scale('A', 'minor')}")
    print(f"G Mixolydian: {generate_scale('G', 'mixolydian')}")
    print(f"F Lydian: {generate_scale('F', 'lydian')}")