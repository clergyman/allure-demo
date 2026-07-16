import { test } from '../fixtures/test';
import * as allure from 'allure-js-commons';

type Severity = 'blocker' | 'critical' | 'normal' | 'minor' | 'trivial';

type ScenarioMetadata = {
  feature: string;
  story: string;
  severity: Severity;
  smoke?: boolean;
};

export function annotateScenario({
  feature,
  story,
  severity,
  smoke = false,
}: ScenarioMetadata) {
  return test.step('Record Allure scenario metadata', async () => {
    await allure.epic('Demo Shop E2E');
    await allure.feature(feature);
    await allure.story(story);
    await allure.layer('e2e');
    await allure.severity(severity);

    void smoke;
  });
}

export async function attachScreenshot(name: string, pageScreenshot: Buffer) {
  await test.info().attach(name, {
    body: pageScreenshot,
    contentType: 'image/png',
  });
  await allure.attachment(name, pageScreenshot, { contentType: 'image/png' });
}
