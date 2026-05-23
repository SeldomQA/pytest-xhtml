const mediaViewer = require('./mediaviewer.js')
const templateResult = document.getElementById('template_results-table__tbody')

function htmlToElements(html) {
    const temp = document.createElement('template')
    temp.innerHTML = html
    return temp.content.childNodes
}

const find = (selector, elem) => {
    if (!elem) {
        elem = document
    }
    return elem.querySelector(selector)
}

const findAll = (selector, elem) => {
    if (!elem) {
        elem = document
    }
    return [...elem.querySelectorAll(selector)]
}

const dom = {
    getResultTBody: ({ testId, id, log, extras, resultsTableRow, tableHtml, result, collapsed }) => {
        const resultBody = templateResult.content.cloneNode(true)
        resultBody.querySelector('tbody').classList.add(result.toLowerCase())
        resultBody.querySelector('tbody').id = testId
        resultBody.querySelector('.collapsible').dataset.id = id

        resultsTableRow.forEach((html) => {
            const t = document.createElement('template')
            t.innerHTML = html
            resultBody.querySelector('.collapsible').appendChild(t.content)
        })

        if (log) {
            // Wrap lines starting with "E" with span.error to color those lines red
            const wrappedLog = log.replace(/^E.*$/gm, (match) => `<span class="error">${match}</span>`)
            resultBody.querySelector('.log').innerHTML = wrappedLog
        } else {
            resultBody.querySelector('.log').remove()
        }

        if (collapsed) {
            resultBody.querySelector('.collapsible > .col-result')?.classList.add('collapsed')
            resultBody.querySelector('.extras-row').classList.add('hidden')
        } else {
            resultBody.querySelector('.collapsible > .col-result')?.classList.remove('collapsed')
        }

        const media = []
        extras?.forEach(({ name, format_type, content }) => {
            if (['image', 'video'].includes(format_type)) {
                media.push({ path: content, name, format_type })
            }

            if (format_type === 'html') {
                resultBody.querySelector('.extraHTML').insertAdjacentHTML('beforeend', `<div>${content}</div>`)
            }
        })
        mediaViewer.setup(resultBody, media)

        // Add custom html from the pytest_xhtml_results_table_html hook
        tableHtml?.forEach((item) => {
            resultBody.querySelector('td[class="extra"]').insertAdjacentHTML('beforeend', item)
        })

        return resultBody
    },
}

module.exports = {
    dom,
    htmlToElements,
    find,
    findAll,
}
