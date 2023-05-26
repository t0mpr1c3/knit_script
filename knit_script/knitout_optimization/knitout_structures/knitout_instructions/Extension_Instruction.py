from knit_script.knitout_optimization.knitout_structures.knitout_instructions.instruction import Instruction, Instruction_Type


class Extension_Instruction(Instruction):

    def __init__(self, code: str):
        super().__init__(Instruction_Type.X)
        self.code = code

    def __str__(self):
        return f"{self.instruction_type} {self.code};{self.comment_str}\n"
