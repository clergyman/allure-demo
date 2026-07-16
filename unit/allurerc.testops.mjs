import { env } from "node:process";

export default {
  name: "Unit Tests TestOps Upload",
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
        launchName: "Unit Tests",
        launchTags: ["unit", "demo-shop"],
        autocloseLaunch: true,
      },
    },
  },
};
