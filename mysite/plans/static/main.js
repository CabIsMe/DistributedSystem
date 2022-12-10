let currentData = null;
    let newRow = null;
    let creatingFlag = false;

    // Numbering order 
    let listSerial = document.querySelectorAll('.list-rows .row')

    for( let i = 0; i < listSerial.length; i++) { 
        listSerial[i].firstElementChild.textContent = i + 1
        let btnEdit = listSerial[i].querySelector('.btn-edit')
        
        if(btnEdit)    
            btnEdit.setAttribute('data-id', i+1);
        
        let btnDelete = listSerial[i].querySelector('.btn-delete')
        
        if(btnDelete)
            btnDelete.setAttribute('data-id', i+1);
    }

    // Handle EVENTs

    let wrapper = document.querySelector('.wrapper')

    wrapper.addEventListener('click', e => {
        let target = e.target

        if(target.closest('.btn-create')) {
            creatingFlag = !creatingFlag
            let listRowsElement = document.querySelector('.list-rows')
            newRow = document.createElement('ul')
            newRow.classList.add('row')
            newRow.classList.add('new-row')

            newRow.innerHTML = ` 
                    <li class="grid-item">${listSerial.length+1}</li>
                    <li class="grid-item"><input type="text"  name="planTitle"  value="" placeholder="Type the Title here..."></li>
                    <li class="grid-item"><input type="text"  name="planContent" value="" placeholder="Type the Content here..."></li>
                    <li class="grid-item"><input type="text"  name="planDescription" value="" placeholder="Type the Description here..." ></li>
                    <li class="grid-item"><input type="text"  name="planTime" value="" placeholder="Type the Time here..."></li>
                 `
            
            newRow.addEventListener('input', e => {
                target = e.target;

                if(target.closest('[name="planTitle"]')) {
                    let val = newRow.querySelector('[name="planTitle"]').value

                    document.querySelector('.section-btn [name="planTitle"]').value = val;
                }

                else if(target.closest('[name="planContent"]')) {
                    let val = newRow.querySelector('[name="planContent"]').value

                    document.querySelector('.section-btn [name="planContent"]').value = val;
                }

                else if(target.closest('[name="planDescription"]')) {
                    let val = newRow.querySelector('[name="planDescription"]').value

                    document.querySelector('.section-btn [name="planDescription"]').value = val;
                }

                else if(target.closest('[name="planTime"]')) {
                    let val = newRow.querySelector('[name="planTime"]').value

                    document.querySelector('.section-btn [name="planTime"]').value = val;
                }
            })

            listRowsElement.appendChild(newRow)

            // Display buttons
            let listBtnElement = target.parentNode;
            listBtnElement.querySelector('.btn-create').classList.add('display-none')
            listBtnElement.querySelector('.btn-add').classList.remove('display-none')
            listBtnElement.querySelector('.btn-cancel').classList.remove('display-none')

        }

        else if(target.closest('.btn-cancel')) {
            creatingFlag = !creatingFlag
            
            let listRowsElement = document.querySelector('.list-rows')
            listRowsElement.removeChild(newRow)
            
            // Display buttons
            let listBtnElement = target.parentNode;
            listBtnElement.querySelector('.btn-create').classList.remove('display-none')
            listBtnElement.querySelector('.btn-add').classList.add('display-none')
            listBtnElement.querySelector('.btn-cancel').classList.add('display-none')
        }

    })  

    