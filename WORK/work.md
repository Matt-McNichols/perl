## Create I/O completion Q

---
  * PRP entry 1:
    * If CDW11.PC is set to '1':
      * field specifies a 64-bit base memory address pointer of the Completion Queue that is physically
        contiguous and is memory page aligned (based on the value in CC.MPS)
    * If CDW11.PC is set to '0':
      * field specifies a PRP List pointer that describes the list of pages that constitute the
        Completion Queue and is memory page aligned (based on the value in CC.MPS)
---
  * CDW10:
    * Bit (31-16): Queue Size <QSIZE> -- supports a size zero or larger, the controller should handle it
                   Refer to section 4.1.3
    * Bit (15:00): Queue Id   <QID> -- his identifier corresponds to the
                   Completion Queue Head Doorbell used for this command (i.e., the value y in section 3.1.12).
                   This value shall not exceed the value reported in the Number of Queues feature
                   (see section 5.14.1.7) for I/O Completion Queues
                     * Note: double check the number of Qs feature before

---
  * CDW11:
    * Bit (31-16): Interrupt Vectors <IV> -- This field indicates interrupt vector to use for this Completion Queue. I
                   This corresponds to the MSI-X or multiple message MSI vector to use. If using single message MSI
                   or pin-based interrupts, then this field shall be cleared to 0h.
    * Bit (15-02): Reserved
    * Bit (01):    Interrupts Enabled <IEN> -- If set to '1', then interrupts are enabled for this Completion Queue. If
                   cleared to ?0?, then interrupts are disabled for this Completion Queue
    * Bit (00):    Physically Contiguous <PC> -- If set to '1', then the Completion Queue is physically contiguous
                   and PRP Entry 1 (PRP1) is the address of a contiguous physical buffer. If cleared to '0', then the
                   Completion Queue is not physically contiguous and PRP Entry 1 (PRP1) is a PRP List pointer. If the
                   queue is located in the Controller Memory Buffer and PC is cleared to '0'

                   * the controller shall fail the command with Invalid Use of Controller Memory Buffer status


## Create I/O Submission Q

---
  * PRP entry 1:
    * If CDW11.PC is set to '1':
      * field specifies a 64-bit base memory address pointer of the Submission Queue that is physically
        contiguous and is memory page aligned (based on the value in CC.MPS)
    * If CDW11.PC is set to '0':
      * field specifies a PRP List pointer that describes the list of pages that constitute the
        Submission Queue and is memory page aligned (based on the value in CC.MPS)

---
  * CDW10:
    * Bit (31-16): Queue Size <QSIZE> -- supports a size zero or larger, the controller should handle it
                   Refer to section 4.1.3
    * Bit (15:00): Queue Id   <QID> -- his identifier corresponds to the
                   Completion Queue Head Doorbell used for this command (i.e., the value y in section 3.1.12).
                   This value shall not exceed the value reported in the Number of Queues feature
                   (see section 5.14.1.7) for I/O Completion Queues
                     * Note: double check the number of Qs feature before
---
  * CDW11:
    * Bit (31-16): Completion Queue ID <CQID> -- This field indicates the identifier of the Completion Queue
                   to utilize for any command completions entries associated with this Submission Queue.
                   The value of 0h (Admin Completion Queue) shall not be specified.If the value specified is 0h or
                   does not correspond to a valid I/O Completion Queue, the controller should return an error of
                   Invalid Queue Identifier.
    * Bit (15-03): Reserved
    * Bit (02-01): Queue Priority <QPRIO> -- This field indicates the priority class to use for commands
                   within this Submission Queue. This field is only used when the weighted round robin with urgent
                   priority class is the arbitration mechanism selected, the field is ignored if weighted round robin
                   with urgent priority class is not used. Refer to section 4.11


                   | Value |  Definition  |
                   |-------|:------------:|
                   |  00b  |  Urgent      |
                   |  01b  |  High        |
                   |  10b  |  Medium      |
                   |  01b  |  Low         |


    * Bit (00):    Physically Contiguous <PC> -- If set to '1', then the Completion Queue is physically contiguous
                   and PRP Entry 1 (PRP1) is the address of a contiguous physical buffer. If cleared to '0', then the
                   Completion Queue is not physically contiguous and PRP Entry 1 (PRP1) is a PRP List pointer. If the
                   queue is located in the Controller Memory Buffer and PC is cleared to '0'

                   * the controller shall fail the command with Invalid Use of Controller Memory Buffer status
