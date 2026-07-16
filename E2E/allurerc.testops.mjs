import { env } from "node:process";

export default {
  name: "E2E Tests TestOps Upload",
  qualityGate: {
    rules: [
      {
        maxFailures: 0,
      },
    ],
  },
  plugins: {
    testops: {
      import: "@allurereport/plugin-testops",
      options: {
        endpoint: env.TESTOPS_URL,
        accessToken: env.TESTOPS_TOKEN,
        projectId: env.TESTOPS_PROJECT_ID,
        launchName: "E2E Tests",
        launchTags: ["e2e", "demo-shop"],
        autocloseLaunch: true,
      },
    },
  },
};
