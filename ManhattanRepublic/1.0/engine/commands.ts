// Command grammar and parser for NovaRoma Playability Layer v1.5
// Pure functions only; no I/O

export type Command = {
  verb: string;
  args: Record<string, any>;
  raw: string;
};

export function parseCommand(input: string): Command {
  // Simple parser: split by first space, treat rest as args string
  const [verb, ...rest] = input.trim().split(" ");
  return {
    verb: verb.toUpperCase(),
    args: {}, // TODO: parse args if needed
    raw: input.trim()
  };
}
