signal → slow → pause → refuse - runtime enforcement rather than arithmetic

state = "signal"

if state == "signal":
    detect()
    state = "slow"

if state == "slow":
    throttle()
    state = "pause"

if state == "pause":
    hold()
    state = "refuse"

if state == "refuse":
    halt_execution()

Python Diagram:
 
Note: Multiplication captures the collapse property (any refusal = 0), but a state machine sequence is truer to your authored rails. It enforces custody structurally, not statistically.

Flow Map
 
Studying it, notice how:
•	Signal is the detection layer — it doesn’t stop execution, but it raises awareness and begins ledgering.
•	Slow throttles throughput, forcing the system to reduce pace while custody checks are applied.
•	Pause is a hard hold — execution cannot continue until custody is confirmed.
•	Refuse collapses execution entirely (G = 0). This is the structural safeguard: if custody fails, the system halts.
•	At each transition, ledger evidence is generated — so every signal, slowdown, pause, or refusal is immutably recorded.
This sequence is best thought of as a state machine rather than arithmetic. Multiplication captures the “collapse to zero” property, but the sequential flow enforces custody in real time.

With Ledger:
# Initial system state
state = "signal"

# Runtime ledger to capture custody transitions
ledger = []

def record(event):
    ledger.append({
        "timestamp": current_time(),
        "event": event,
        "state": state
    })

def current_time():
    # Placeholder for actual timestamp logic
    return "2026-02-03T17:55:00Z"

# Signal stage: detection begins
if state == "signal":
    record("Signal detected")
    state = "slow"

# Slow stage: throttle execution
if state == "slow":
    record("Execution throttled")
    state = "pause"

# Pause stage: hold until custody confirmed
if state == "pause":
    custody_confirmed = check_custody()
    if not custody_confirmed:
        state = "refuse"
    else:
        record("Custody confirmed")
        state = "execute"

# Refuse stage: halt execution
if state == "refuse":
    record("Custody failed — execution halted")
    halt_execution()

# Execute stage: proceed only if custody confirmed
if state == "execute":
    record("Execution authorized")
    run_system()

def check_custody():
    # Placeholder for custody verification logic
    return False  # Simulate custody failure

def halt_execution():
    print("System halted due to refusal rail")

def run_system():
    print("System executing with custody enforced")

 
Key Properties:
•	Ledger entries are recorded at every transition — immutable, timestamped, and state-bound.
•	Custody check is enforced before execution — refusal halts the system.
•	No reconstruction — every decision point is captured live, not inferred later.

