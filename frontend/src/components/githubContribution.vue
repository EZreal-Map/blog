<template>
  <div class="container" v-show="datas">
    <div
      v-for="(weeks, weekIndex) in datas?.weeks"
      :key="weekIndex"
      class="weeks"
    >
      {{ weekIndex }}
      <div
        v-for="cell in weeks.contributionDays"
        :key="cell.firstDay"
        class="cell"
        :style="{ backgroundColor: cell.color }"
        :title="`${cell.contributionCount === 0 ? 'No contribution' : cell.contributionCount + ' contributions'} on ${cell.date}`"
      ></div>
    </div>
  </div>
</template>
<script setup>
import axios from 'axios'
import { shallowRef } from 'vue'
import { githubApiKey, githubName } from '/secret.js' // 从前端项目根目录 secret.js 中导入 githubApiKey
let datas = shallowRef(null)

// 使用 async/await 处理异步代码
;(async () => {
  try {
    const { data } = await getContributions(githubApiKey, githubName)
    console.log('hello')

    datas.value = data.user.contributionsCollection.contributionCalendar
    console.log(datas.value)
  } catch (error) {
    // 处理错误
  }
})()

async function getContributions(token, username) {
  const headers = {
    Authorization: `bearer ${token}`,
    'Content-Type': 'application/json'
  }

  const query = `
    query {
      user(login: "${username}") {
        name
        contributionsCollection {
          contributionCalendar {
            colors
            totalContributions
            weeks {
              contributionDays {
                color
                contributionCount
                date
                weekday
              }
              firstDay
            }
          }
        }
      }
    }
  `

  try {
    const { data } = await axios.post(
      'https://api.github.com/graphql',
      { query },
      { headers }
    )
    return data
  } catch (error) {
    console.error('Error fetching data:', error.message)
    throw error
  }
}
</script>
<style scoped>
.container {
  display: flex;
  flex-direction: row;
  background-color: #fff;
}

.weeks {
  display: flex;
  flex-direction: column;
}

.cell {
  width: 16px;
  height: 16px;
  background-color: green;
  margin: 2px; /* Add some margin for better visualization */
}
</style>
