# rpa_ops — Controlled Browser Automation

## When to use

Use this skill when a task requires controlled browser inspection, screenshots, navigation, or clicking/type actions.

## Owner rule

CDP jobs must use an allowed owner. If `玄策DT` is rejected, use an allowed operational owner such as `luban`, only when appropriate.

## Safety rule

Navigation and observation are lower risk. Clicking, typing, submitting, saving, buying, deleting, or changing external state requires explicit task intent and evidence.

## Procedure

1. Probe browser target.
2. Navigate if needed.
3. Snapshot or screenshot before action.
4. For external write actions, confirm selector and expected effect.
5. Execute one small action at a time.
6. Capture evidence after action.
7. Report whether `external_write_executed` is true or false.

## Completion

Only completed if broker returns:

- `status: completed`
- `result.ok: true`
- relevant evidence path

## Failure modes

- not logged in
- owner not allowed
- selector missing
- page changed
- external write blocked
- captcha / auth challenge
