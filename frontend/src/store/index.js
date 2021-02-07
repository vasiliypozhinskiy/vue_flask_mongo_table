import Vue from 'vue'
import Vuex from 'vuex'
import axios from "axios";

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        token: localStorage.getItem('user-token') || '',
        username: localStorage.getItem('username') || '',
        table: []
    },
    mutations: {
        "AUTH_SUCCESS": (state, {username, token}) => {
            state.token = token;
            state.username = username;
        },
        "AUTH_LOGOUT": (state) => {
            state.token = '';
            state.username = '';
        },
        "SOCKET_CHANGE_STATUS": (state, data) => {
            let ids = data.ids
            let value = data.value
            ids.forEach(id => {
                for (let i = 0; i < state.table.length; i++) {
                    if (state.table[i]._id.$oid === id) {
                        state.table[i].status = value
                    }
                }
            })
        },
        "SOCKET_CHANGE_TITLE": (state, data) => {
            for (let i = 0; i < state.table.length; i++) {
                if (state.table[i]._id.$oid === data.id)
                    state.table[i].title = data.value
            }
        },
        "SOCKET_CHANGE_DATE": (state, data) => {
            for (let i = 0; i < state.table.length; i++) {
                if (state.table[i]._id.$oid === data.id)
                    state.table[i].date = data.value
            }
        },
        "SOCKET_CHANGE_NUMBER": (state, data) => {
            for (let i = 0; i < state.table.length; i++) {
                if (state.table[i]._id.$oid === data.id)
                    state.table[i].number = data.value
            }
        },
        "SOCKET_ADD_ROW": (state, data) => {
            let newRow = JSON.parse(data)
            newRow.isChecked = false;
            state.table.push(newRow);
        },
        "SOCKET_DELETE_ROWS": (state, ids) => {
            ids.forEach(id => {
                for (let i = 0; i < state.table.length; i++) {
                    if (state.table[i]._id.$oid === id) {
                        state.table.splice(i, 1);
                    }
                }
            })
        },
        "SAVE_TABLE": (state, newTable) => {
            for (let i = 0; i < newTable.length; i++) {
                let newRow = newTable[i]
                newRow.isChecked = false;
                Vue.set(state.table, i, newRow)
            }
        },
        "CHANGE_CHECKBOX": (state, {index, value}) => {
            state.table[index].isChecked = value;
        },
        "CHANGE_ALL_CHECKBOX": (state, value) => {
            for (let i = 0; i < state.table.length; i++) {
                state.table[i].isChecked = value
            }
        }
    },
    actions: {
        "LOAD_TABLE": ({commit, state}) => {
            axios.get('http://localhost:80/api/get-table',
                {headers: {'Authorization': state.token, "Username": state.username}})
                .then(response => {
                    commit('SAVE_TABLE', response.data.table);
                })
        },
        "AUTH_REQUEST": ({commit}, user) => {
            return new Promise((resolve, reject) => {
                axios({url: 'http://127.0.0.1:80/api/get-token', data: user, method: 'POST'})
                    .then((response) => {
                        const token = response.data.token
                        localStorage.setItem('user-token', token)
                        localStorage.setItem('username', user.username)
                        commit("AUTH_SUCCESS", {"token": token, "username": user.username})
                        resolve(response)
                    })
                    .catch(err => {
                        localStorage.removeItem('user-token')
                        reject(err)
                    })
            })
        },
        "AUTH_LOGOUT": ({commit}) => {
            return new Promise((resolve) => {
                commit("AUTH_LOGOUT")
                localStorage.removeItem('user-token') // clear your user's token from localstorage
                resolve()
            })
        },
        SAVE_ONE_CELL_IN_DB({state}, {index, value}) {
            let id = state.table[index]._id.$oid
            this._vm.$socket.emit("CHANGE_CELL", {id, value})
        },
        ADD_ROW_IN_DB() {
            let today = new Date(Date.now()).toISOString();
            today = today.substr(0, 10)
            this._vm.$socket.emit("ADD_ROW", today)
        },
        DELETE_ROWS_FROM_DB() {
            let ids = []
            for (let i = 0; i < this.state.table.length; i++) {
                if (this.state.table[i].isChecked) {
                    ids.push(this.state.table[i]._id.$oid)
                }
            }
            this._vm.$socket.emit("DELETE_ROWS", ids)
        },
        SAVE_MANY_CELLS_IN_DB({state}, {index, value}) {
            let ids = [state.table[index]._id.$oid]
            for (let i = 0; i < state.table.length; i++) {
                if (state.table[i].isChecked) {
                    ids.push(state.table[i]._id.$oid)
                }
            }
            this._vm.$socket.emit("CHANGE_CELLS", {ids, value})
        }
    },
    modules: {},
    getters: {
        isAuthenticated: state => !!state.token
    }
})
