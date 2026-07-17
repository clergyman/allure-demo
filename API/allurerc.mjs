export default {
  name: "API Tests Allure Report",
  output: "./allure-report",
  historyPath: "./history.jsonl",
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
    awesome: {
      options: {
        reportName: "API Tests Allure Report",
        singleFile: true,
        reportLanguage: "en",
        open: false,
        publish: true,
      },
    },
  },
};
