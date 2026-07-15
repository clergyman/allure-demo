import { env } from "node:process";

export default {
  name: "API Tests TestOps Upload",
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
        launchName: env.TESTOPS_LAUNCH_NAME || "API Tests",
        launchTags: ["api", "demo-shop"],
        autocloseLaunch: true,
      },
    },
  },
};
