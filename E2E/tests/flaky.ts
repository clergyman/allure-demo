export function maybeFlake(probability: number, scenario: string) {
  if (process.env.DEMO_DISABLE_FLAKES === '1') {
    return;
  }

  if (Math.random() < probability) {
    throw new Error(
      `Demo flaky failure (${Math.round(probability * 100)}% chance): ${scenario}`,
    );
  }
}
