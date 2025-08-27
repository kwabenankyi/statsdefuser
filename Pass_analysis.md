# Pass data
## Pass Attributes

### Basic Attributes
- **recipient**: object player(id: int, name: str)
- **length**: double
- **angle**: double
- **height**: enum pass_height {1: "Ground", 2: "Low", 3: "High"}
- **end_location**: (int, int)
- **body_part**: enum pass_body_part {68: "Drop Kick", 37: "Head", 69: "Keeper Arm", 38: "Left Foot", 70: "Other", 40: "Right Foot", 106: "No Touch"}

### Additional Attributes
- **assisted_shot_id**: uuid - Reference to the shot this pass assisted
- **backheel**: boolean - Added if the pass was made by using a backheel
- **deflected**: boolean - Added if the pass was deflected
- **miscommunication**: boolean - Added if the pass was a miscommunication
- **cross**: boolean - Added if the pass was a cross
- **cut-back**: boolean - Added if the pass was a cut-back
- **switch**: boolean - Added if the pass was a switch
- **shot-assist**: boolean - Added if the pass was an assist to a shot
- **goal-assist**: boolean - Added if the pass was an assist to a goal
- **outcome**: enum pass_outcome {9: "Incomplete", 74: "Injury Clearance", 75: "Out", 76: "Pass Offside", 77: "Unknown"} - Added if pass not completed
- **pass_type**: enum pass_type {61: "Corner", 62: "Free Kick", 63: "Goal Kick", 64: "Interception", 65: "Kick Off", 66: "Recovery", 67: "Throw-in"} - Added if pass type atypical
- **technique**: enum pass_technique {104: "Inswinging", 105: "Outswinging", 107: "Straight", 108: "Through Ball"} - Added if corner or through ball