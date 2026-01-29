// Reducers for NovaRoma Playability Layer v1.5
// Pure functions: (state, command) => { newState, events, outputs }

export function statusReducer(state, command) {
  // Example: return status report markdown, no state change
  return {
    newState: state,
    events: [{ event_type: "COMMAND", command: "STATUS", payload: { target: command.args.target } }],
    outputs: [`Status — ${command.args.target || "unknown"}`]
  };
}

// TODO: Implement other reducers (siteReportReducer, initiativeCreateReducer, etc.)
