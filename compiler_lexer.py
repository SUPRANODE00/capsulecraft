import re

class Lexer:
    def __init__(self, source_code):
        self.source = source_code
        self.tokens = []
        
    def tokenize(self):
        token_specification = [
            ('NUMBER',   r'\d+'),
            ('ASSIGN',   r'='),
            ('ID',       r'[A-Za-z_][A-Za-z0-9_]*'),
            ('PLUS',     r'\+'),
            ('MINUS',    r'-'),
            ('MUL',      r'\*'),
            ('DIV',      r'/'),
            ('LPAREN',   r'\('),
            ('RPAREN',   r'\)'),
            ('SKIP',     r'[ \t\n]+'),
            ('MISMATCH', r'.'),
        ]
        
        tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)
        get_token = re.compile(tok_regex).match
        match = get_token(self.source)
        
        pos = 0
        while match:
            kind = match.lastgroup
            value = match.group(kind)
            if kind == 'SKIP':
                pass
            elif kind == 'MISMATCH':
                raise RuntimeError(f'{value!r} unexpected on character index {pos}')
            else:
                self.tokens.append({"type": kind, "value": value})
            pos = match.end()
            match = get_token(self.source, pos)
            
        print(f"Tokenization complete: {len(self.tokens)} tokens extracted safely.")
        return self.tokens

if __name__ == "__main__":
    lexer = Lexer("CONFIG_SECRET = 800 + 400")
    tokens = lexer.tokenize()
    print("Generated Token Stream:", tokens)
