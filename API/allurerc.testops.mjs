import { env } from "node:process";

export default {
  name: "API Tests TestOps Upload",
  categories: {
    rules: [
      {
        name: "API failures by severity and component",
        id: "api-failures-by-severity-and-component",
        matchers: {
          statuses: ["failed", "broken"],
        },
        groupBy: ["severity", { label: "component" }],
        groupByMessage: true,
        expand: true,
      },
    ],
  },
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
